from django.conf.urls import patterns, url
from .views import ResumeView, CreatorView
from .models import Resume

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[a-z-]+)/',
        ResumeView.as_view(template_name='resume/resume.html',
                           model=Resume),
        name='index'),
    url(r'^add-new',
        CreatorView.as_view(template_name='resume/creator.html'),
        name='add-new'),
)
