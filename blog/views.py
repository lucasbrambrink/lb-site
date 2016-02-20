from django.views.generic import TemplateView
from django.shortcuts import render
from .models import BlogPost


class BlogIndex(TemplateView):
    template_name = 'blog/landing.html'

    def get(self, request, *args, **kwargs):
        published_posts = BlogPost.published.all()
        return render(request, self.template_name, {
            'posts': published_posts
        })