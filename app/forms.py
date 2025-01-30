# app/forms.py
from django import forms
from .models import IncidentReport, Household, Resident, BarangayEvent, Official

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['title', 'description', 'location', 'reported_by', 'involved_residents', 'events']

class HouseholdForm(forms.ModelForm):
    head = forms.ModelChoiceField(
        queryset=Resident.objects.all(), 
        required=True, 
        label="Head of Household"
    )

    members = forms.ModelMultipleChoiceField(
        queryset=Resident.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # ⬅ Checkbox for members
        required=False,
        label="Household Members"
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter household address'}),
        required=True
    )

    class Meta:
        model = Household
        fields = ['household_name', 'head', 'address', 'members']
class ResidentForm(forms.ModelForm):
    events = forms.ModelMultipleChoiceField(
        queryset=BarangayEvent.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'gender', 'birthdate', 'address', 'household', 'events']

class OfficialForm(forms.ModelForm):
    resident = forms.ModelChoiceField(
        queryset=Resident.objects.all(), 
        required=False, 
        empty_label="Select Resident"
    )

    class Meta:
        model = Official
        fields = ['position', 'contact_number', 'term_start', 'term_end', 'resident']
