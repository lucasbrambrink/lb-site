from .models import Resume, ResumeCategory
from common.views import GenericModelView


class ResumeView(GenericModelView):

    def get_context_data(self, request=None, slug=None, **kwargs):
        context = {
            'render_static': request.GET.get('q', '') == 'static'
        }
        model = self.get_model(slug)
        if not model:
            return context

        category = request.GET.get('category', '')
        if category:
            try:
                instance = ResumeCategory.objects.get(category=category)
                model.set_instance_category(instance)
            except ResumeCategory.DoesNotExist:
                pass

        context[self.model_kwarg] = model
        return context

