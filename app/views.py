from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Resident, Official, BarangayEvent, IncidentReport, Household 
from .forms import IncidentReportForm
from .forms import OfficialForm
from .models import Household
from .forms import HouseholdForm


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ResListView(ListView):
    model = Resident
    context_object_name = 'residents'
    template_name = 'app/res_list.html'

class ResDetailed(DetailView):
    model = Resident
    context_object_name = 'resident'
    template_name = 'app/res_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resident = self.object
        context['household'] = resident.household  # Add the household to the context
        return context


class ResCreateView(CreateView):
    model = Resident
    fields = ['first_name', 'last_name', 'gender', 'birthdate', 'address', 'household']
    template_name = 'app/res_create.html'

    def get_initial(self):
        # Pre-fill the household field if household_id is provided in the URL
        initial = super().get_initial()
        household_id = self.request.GET.get('household_id')
        if household_id:
            initial['household'] = get_object_or_404(Household, pk=household_id)
        return initial

def get_success_url(self):
    household = self.object.household
    if household:
        return reverse_lazy('household_detail', kwargs={'pk': household.pk})
    return reverse_lazy('res_list')  # Default to resident list


    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class ResUpdateView(UpdateView):
    model = Resident
    fields = ['first_name', 'last_name']
    template_name = 'app/res_update.html'
    success_url = reverse_lazy('res_list')


class ResDeleteView(DeleteView):
    model = Resident
    template_name = 'app/res_delete.html'
    success_url = reverse_lazy('res_list')


class OfficialListView(ListView):
    model = Official
    context_object_name = 'officials'
    template_name = 'app/official_list.html'

class OfficialDetailView(DetailView):
    model = Official
    context_object_name = 'official'
    template_name = 'app/official_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        official = self.object  # The current official instance
        context['events'] = official.events.all()  # Reverse lookup using related_name
        return context

class OfficialCreateView(CreateView):
    model = Official
    form_class = OfficialForm  # Only use form_class to specify the form
    template_name = 'app/official_create.html'
    success_url = reverse_lazy('official_list')
    

class OfficialUpdateView(UpdateView):
    model = Official
    fields = ['position', 'first_name', 'last_name', 'contact_number', 'term_start', 'term_end']
    template_name = 'app/official_update.html'
    success_url = reverse_lazy('official_list')

class OfficialDeleteView(DeleteView):
    model = Official
    template_name = 'app/official_delete.html'
    success_url = reverse_lazy('official_list')

class EventListView(ListView):
    model = BarangayEvent
    template_name = 'app/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = BarangayEvent
    context_object_name = 'event'
    template_name = 'app/event_detail.html'

class EventCreateView(CreateView):
    model = BarangayEvent
    fields = ['event_name', 'description', 'date', 'location']
    template_name = 'app/event_form.html'
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = BarangayEvent
    fields = ['event_name', 'description', 'date', 'location']
    template_name = 'app/event_form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = BarangayEvent
    template_name = 'app/event_delete.html'
    success_url = reverse_lazy('event_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("Event not found")
        return obj

def incident_create(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            incident = form.save()

            # Associating events (example)
            event_ids = request.POST.getlist('events')  # assuming 'events' is the name of the checkbox field
            events = BarangayEvent.objects.filter(id__in=event_ids)
            incident.events.set(events)  # Associate events with the incident
            incident.save()

            return redirect('incident_list')
    else:
        form = IncidentReportForm()

    return render(request, 'app/incident_form.html', {'form': form})

def incident_list(request):
    incidents = IncidentReport.objects.all()
    return render(request, 'app/incident_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    incident = get_object_or_404(IncidentReport, pk=pk)
    return render(request, 'app/incident_detail.html', {'incident': incident})

# Household List View
class HouseholdListView(ListView):
    model = Household
    template_name = 'app/household_list.html'
    context_object_name = 'households'

# Household Detail View
class HouseholdDetailView(DetailView):
    model = Household
    template_name = 'app/household_detail.html'
    context_object_name = 'household'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        household = self.object
        context['members'] = household.resident_set.all()  # Get all residents of the household
        return context


# Household Create View
class HouseholdCreateView(CreateView):
    model = Household
    form_class = HouseholdForm  # Use the HouseholdForm
    template_name = 'app/household_create.html'
    success_url = reverse_lazy('household_list')

# Household Update View
class HouseholdUpdateView(UpdateView):
    model = Household
    form_class = HouseholdForm  # This will use the HouseholdForm to render the update form
    template_name = 'app/household_update.html'  # The template for rendering the form
    success_url = reverse_lazy('household_list')

# Household Delete View
class HouseholdDeleteView(DeleteView):
    model = Household
    template_name = 'app/household_delete.html'
    success_url = reverse_lazy('household_list')
