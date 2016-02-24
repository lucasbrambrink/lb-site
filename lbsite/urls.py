from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resume/', include('resume.urls', namespace='resume')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('resume:index',
                                                     kwargs={'slug': 'lucas-brambrink'})))
)
