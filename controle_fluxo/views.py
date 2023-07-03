from django.shortcuts import render
from django.views.generic import TemplateView, FormView
# from django.views import View
# from .models import activities
from django.urls import reverse_lazy
from .forms import ActivitiesForm

class IndexView(TemplateView):
    template_name = 'index.html'
    
class CreateActivy(FormView):
    template_name = 'create_activity.html'
    form_class = ActivitiesForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CreateActivy, self).get_context_data(**kwargs)
        context['form'] = ActivitiesForm()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.save()
        print('cadastrou')
        return super(CreateActivy, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        print('não cadastrou')
        return super(CreateActivy, self).form_invalid(form, *args, **kwargs)
