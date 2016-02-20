from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$',
        view=TemplateView.as_view(template_name='home/index.html'),
        name='landing'),
    url(r'^$',
        view=TemplateView.as_view(template_name='home/about.html'),
        name='about'),
)
