from django.db import models


class ContactInfo(models.Model):
    street = models.CharField(max_length=255)
    city_state = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __unicode__(self):
        return self.email


class Education(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    completion_date = models.CharField(max_length=255)
    description = models.TextField()
    resume = models.ForeignKey('Resume')

    def __unicode__(self):
        return self.title


class Line(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text


class CareerGoal(models.Model):
    goal = models.TextField()

    def __unicode__(self):
        return self.goal


class ProgrammingSkills(models.Model):
    title = models.CharField(max_length=255)
    lines = models.ManyToManyField(to='Line')
    resume = models.ForeignKey('Resume')

    def __unicode__(self):
        return self.title


class WorkExperience(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dates = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    skills = models.TextField()
    bullets = models.ManyToManyField(to='Line')
    resume = models.ForeignKey('Resume')

    def __unicode__(self):
        return self.title


class Resume(models.Model):
    name = models.CharField(max_length=255)
    contact = models.ForeignKey(to='ContactInfo', null=True)
    career_goal = models.ForeignKey(to='CareerGoal', null=True)
    slug = models.SlugField(default='')

    @property
    def education(self):
        return self.education_set.order_by('pk').values()

    @property
    def programming(self):
        return self.programmingskills_set.order_by('pk')

    @property
    def experience(self):
        return self.workexperience_set.order_by('pk')

    def __unicode__(self):
        return self.name

    @property
    def contact_info(self):
        return self.contact


def create_initial_resume():
    from .conf import LUCAS_BRAMBRINK
    resume = Resume()
    resume.save()
    key_model_map = {
        'contact': ContactInfo,
        'experience': WorkExperience,
        'career_goal': CareerGoal,
        'education': Education,
        'programming': ProgrammingSkills,
    }

    def encode_dict(model_class, resume, dictionary):
        new_model = model_class()
        new_model.resume = resume
        for key, attr in dictionary.items():
            if not type(attr) is list:
                setattr(new_model, key, attr)
                continue

            lines = [
                Line(text=list_element) for list_element in attr
            ]
            for line in lines:
                line.save()

            new_model.save()
            setattr(new_model, key, lines)
            print key, new_model.__dict__, lines
            new_model.save()
            continue

        new_model.save()

    for fk, value in LUCAS_BRAMBRINK.items():
        if type(value) is str:
            setattr(resume, fk, value)
            continue

        model_class = key_model_map[fk]
        if type(value) is dict:
            encode_dict(model_class, resume, value)
            continue

        if type(value) is list:
            for object_ in value:
                if type(object_) is dict:
                    print object_
                    encode_dict(model_class, resume, object_)

    resume.save()


