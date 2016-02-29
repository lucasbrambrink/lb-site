from django.db import models
from django.db.models import Q
from common.utils import truncate_chars


class SortingValueMixin(models.Model):
    sorting_value = models.IntegerField(default=1)

    class Meta:
        abstract = True
        ordering = ['sorting_value']


class ResumeCategory(models.Model):
    """
    e.g finance, frontend, backend, business, design
    """
    category = models.CharField(max_length=255)

    def __unicode__(self):
        return self.category


class ContactInfo(models.Model):
    street = models.CharField(max_length=255)
    city_state = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __unicode__(self):
        return self.email


class Education(SortingValueMixin):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    completion_date = models.CharField(max_length=255)
    description = models.TextField()
    resume = models.ForeignKey('Resume')
    categories = models.ManyToManyField('ResumeCategory',
                                        blank=True)

    def __unicode__(self):
        return self.title


class Line(SortingValueMixin):
    text = models.TextField()

    def __unicode__(self):
        return truncate_chars(self.text, 30)


class CareerGoal(SortingValueMixin):
    goal = models.TextField()
    resume = models.ForeignKey(to='Resume', null=True)
    categories = models.ManyToManyField('ResumeCategory',
                                        blank=True)

    def __unicode__(self):
        return truncate_chars(self.goal, 30)


class ProgrammingSkills(SortingValueMixin):
    title = models.CharField(max_length=255)
    lines = models.ManyToManyField(to='Line')
    resume = models.ForeignKey('Resume')
    categories = models.ManyToManyField('ResumeCategory',
                                        blank=True)

    def __unicode__(self):
        return self.title


class WorkExperience(SortingValueMixin):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dates = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    skills = models.TextField()
    bullets = models.ManyToManyField(to='Line')
    resume = models.ForeignKey('Resume')
    categories = models.ManyToManyField('ResumeCategory',
                                        blank=True)

    def __unicode__(self):
        return self.title


class Resume(models.Model):
    name = models.CharField(max_length=255)
    contact = models.ForeignKey(to='ContactInfo', null=True)
    slug = models.SlugField(default='')
    categories = models.ManyToManyField('ResumeCategory', blank=True)

    def by_categories(self, qs=None):
        return qs.filter(
            Q(categories__category=self.instance_category) |
            Q(categories__isnull=True) |
            Q(categories__category=u'always_show')
        ).order_by(u'sorting_value')

    def __init__(self, *args, **kwargs):
        super(Resume, self).__init__(*args, **kwargs)
        self.set_instance_category()

    def set_instance_category(self, category_kwarg=None):
        self.instance_category = self.categories.first()
        try:
            self.instance_category = ResumeCategory.objects\
                .get(category=category_kwarg or u'general')
        except ResumeCategory.DoesNotExist:
            pass

        for attr, qs in ((u'education', self.education_set),
                         (u'career_goal', self.careergoal_set),
                         (u'programming', self.programmingskills_set),
                         (u'experience', self.workexperience_set)):
            setattr(self, attr, self.by_categories(qs.all()))

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


