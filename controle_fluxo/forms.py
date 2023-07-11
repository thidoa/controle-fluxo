from django import forms
from .models import Activities, Bank, Owner

class ActivitiesForm(forms.Form):
    value = forms.DecimalField(required=True)
    input = forms.BooleanField(required=False)
    description = forms.CharField(max_length=200, required=True, widget=forms.Textarea)
    bank = forms.ModelChoiceField(queryset=Bank.objects.all())
    owner = forms.ModelChoiceField(queryset=Owner.objects.all())
    proof = forms.FileField(required=False)

    def save(self):
        activities = Activities(
            value = self.cleaned_data['value'],
            input = self.cleaned_data['input'],
            description = self.cleaned_data['description'],
            bank = self.cleaned_data['bank'],
            owner = self.cleaned_data['owner'],
            proof = self.cleaned_data['proof']
        )

        activities.save()

    