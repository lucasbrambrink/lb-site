from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class GenericModelView(TemplateView):
    model = None
    model_kwarg = None

    @classmethod
    def as_view(cls, model=None, model_kwarg=None, **initkwargs):
        cls.model = model
        if cls.model is None:
            raise NotImplementedError('Model class is not declared')

        cls.model_kwarg = model_kwarg or cls.model._meta.model_name
        super(GenericModelView, cls).as_view(**initkwargs)

    def get_context_data(self, request=None, **kwargs):
        return {}

    def get(self, request, slug=None, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)

        try:
            context[self.model_kwarg] = self.model.objects.get(slug=slug)
        except self.model.DoesNotExist:
            return HttpResponse('Unable to resolve database model based on provided URL')

        return render(request, self.template_name, context)

