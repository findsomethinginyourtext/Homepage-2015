from django.views import generic

from .models import FlatPage

class HomeView(generic.TemplateView):
    """
    TODO
    """
    template_name = 'home.html'

    def get_context_data(self, **context):
        context = super().get_context_data(**context)
        context['flatpages'] = FlatPage.objects.all()
        return context


class FlatPageView(generic.DetailView):
    """
    TODO
    """
    model = FlatPage
    template_name = 'flatpage_default.html'

    def get_context_data(self, **context):
        context = super().get_context_data(**context)
        context['flatpages'] = FlatPage.objects.all()
        return context