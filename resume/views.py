from .models import Resume
from common.views import GenericModelView


class ResumeView(GenericModelView):

    def get_context_data(self, request=None, **kwargs):
        return {
            'render_static': request.GET.get('q', '') == 'static'
        }