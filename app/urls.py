from django.urls import path  # Ensure this line is at the top of the file
from . import views  # Import views

from .views import (
    HomePageView, AboutPageView,
    ResListView, ResDetailed, ResCreateView, ResUpdateView, ResDeleteView,
    OfficialListView, OfficialDetailView, OfficialCreateView, OfficialUpdateView, OfficialDeleteView,
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    HouseholdListView, HouseholdDetailView, HouseholdCreateView, HouseholdUpdateView, HouseholdDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
   
    path('res/', ResListView.as_view(), name='res_list'),
    path('res/<int:pk>/', ResDetailed.as_view(), name='res_detail'),
    path('res/create/', ResCreateView.as_view(), name='res_create'),
    path('res/<int:pk>/edit/', ResUpdateView.as_view(), name='res_update'),
    path('res/<int:pk>/delete/', ResDeleteView.as_view(), name='res_delete'),
   
    path('officials/', OfficialListView.as_view(), name='official_list'),
    path('officials/<int:pk>/', OfficialDetailView.as_view(), name='official_detail'),
    path('officials/create/', OfficialCreateView.as_view(), name='official_create'),
    path('officials/<int:pk>/edit/', OfficialUpdateView.as_view(), name='official_update'),
    path('officials/<int:pk>/delete/', OfficialDeleteView.as_view(), name='official_delete'),

    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

    path('incident/create/', views.incident_create, name='incident_create'),
    path('incident/', views.incident_list, name='incident_list'),
    path('incidents/<int:pk>/', views.incident_detail, name='incident_detail'),
    

    path('households/', HouseholdListView.as_view(), name='household_list'),
    path('households/<int:pk>/', HouseholdDetailView.as_view(), name='household_detail'),
    path('households/new/', HouseholdCreateView.as_view(), name='household_create'),
    path('households/<int:pk>/edit/', HouseholdUpdateView.as_view(), name='household_update'),
    path('households/<int:pk>/delete/', HouseholdDeleteView.as_view(), name='household_delete'),
]
