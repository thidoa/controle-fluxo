from django import forms
from .models import Activities, Bank, Owner

class ActivitiesForm(forms.Form):
    value = forms.DecimalField(required=True, widget=forms.TextInput(attrs={'class':'bg-dark'}))
    input = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'bg-dark border border-light'}))
    description = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={'class':'bg-dark'}))
    bank = forms.ModelChoiceField(queryset=Bank.objects.all(), widget=forms.Select(attrs={'class':'bg-dark text-light'}))
    owner = forms.ModelChoiceField(queryset=Owner.objects.all(), widget=forms.Select(attrs={'class':'bg-dark text-light'}))
    proof = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class':'bg-dark text-light'}))

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

    