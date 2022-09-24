from django.views.generic import TemplateView


class MyView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
