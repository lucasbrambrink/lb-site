from django.conf.urls import patterns, url
from .views import ResumeView
from .models import Resume

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[a-z-]+)/',
        view=ResumeView.as_view(template_name='resume/resume.html',
                                model=Resume),
        name='index'),
)
