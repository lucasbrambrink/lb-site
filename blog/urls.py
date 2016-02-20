from django.conf.urls import patterns, url
from .views import BlogIndex
from common.views import GenericModelView
from .models import BlogPost

urlpatterns = patterns(
    '',
    url(r'^$', BlogIndex.as_view(), name='landing'),
    url(r'^(?P<slug>[a-z-]+)/',
        view=GenericModelView.as_view(template_name='blog/entry_base.html',
                                      model=BlogPost,
                                      model_kwarg='post'),
        name='entry'),
)
