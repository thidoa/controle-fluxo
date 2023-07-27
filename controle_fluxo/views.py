from django.shortcuts import render
from django.views.generic import TemplateView, FormView
# from django.views import View
from .models import Activities, Bank, Owner
from django.urls import reverse_lazy
from .forms import ActivitiesForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['owners'] = Owner.objects.all()
        context['banks'] = Bank.objects.all()
        return context

class CreateActivity(FormView):
    template_name = 'create_activity.html'
    form_class = ActivitiesForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CreateActivity, self).get_context_data(**kwargs)
        context['form'] = ActivitiesForm()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.save()
        self.update_contas()
        return super(CreateActivity, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        print('não cadastrou')
        return super(CreateActivity, self).form_invalid(form, *args, **kwargs)
    
    def update_contas(self):
        banks = Bank.objects.all()
        owners = Owner.objects.all()

        activities = Activities.objects.all()

        # *********** REMEMBER ************
        # Duplicate code
        for bank in banks:
            bank.value = 0
            for activitie in activities:
                if str(activitie.bank) == str(bank.name):
                    if activitie.input:
                        bank.value += activitie.value
                    else:
                        bank.value -= activitie.value
                    bank.save()
        
        for owner in owners:
            owner.value = 0
            
            for activitie in activities:
                if str(activitie.owner) == str(owner.name):
                    if activitie.input:
                        owner.value += activitie.value
                    else:
                        owner.value -= activitie.value
                    owner.save()

class HistoricView(TemplateView):
    template_name = 'historic.html'

    def get(self, request, name):
        
        if Owner.objects.filter(name=name).exists():
            historic = Activities.objects.filter(owner=(Owner.objects.filter(name=name)).first())
            total = Owner.objects.filter(name=name).first().value
        elif Bank.objects.filter(name=name).exists():
            historic = Activities.objects.filter(bank=(Bank.objects.filter(name=name)).first())
            total = Bank.objects.filter(name=name).first().value
        else:
            historic = Activities.objects.all()
            total = 0
        print(historic)
        
        context = {
            'historic': historic,
            'total': total
        }
        return render (request, 'historic.html', context)

    # def get_context_data(self, **kwargs):
    #     context = super(HistoricView, self).get_context_data(**kwargs)
    #     context['historic'] = Activities.objects.all()
    #     return context