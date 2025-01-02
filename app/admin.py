from django.contrib import admin
from .models import Resident, Official, BarangayEvent, Household, IncidentReport

admin.site.register(Resident)
admin.site.register(Official)
admin.site.register(BarangayEvent)
admin.site.register(Household)
admin.site.register(IncidentReport)