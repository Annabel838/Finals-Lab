# app/forms.py
from django import forms
from .models import IncidentReport
from .models import Household
from .models import Resident,  BarangayEvent, IncidentReport, Official

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['title', 'description', 'location', 'reported_by', 'involved_residents']

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['household_name', 'head', 'address']

    def clean(self):
        cleaned_data = super().clean()
        
        # You can add custom validation logic here
        head = cleaned_data.get('head')

        # Check if the head of the household is already assigned to another household
        if Household.objects.filter(head=head).exists():
            raise forms.ValidationError("The head of the household is already assigned to another household.")

        return cleaned_data

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'gender', 'birthdate', 'address', 'household', 'events']
        events = forms.ModelMultipleChoiceField(queryset=BarangayEvent.objects.all(), widget=forms.CheckboxSelectMultiple)

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['title', 'description', 'location', 'reported_by', 'involved_residents', 'events']

class OfficialForm(forms.ModelForm):
    class Meta:
        model = Official
        fields = ['position', 'contact_number', 'term_start', 'term_end', 'resident']

    resident = forms.ModelChoiceField(queryset=Resident.objects.all(), required=False, empty_label="Select Resident")