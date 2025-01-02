from django.db import models
from django.urls import reverse
from django.utils import timezone

class Household(models.Model):
    household_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    head = models.ForeignKey('Resident', on_delete=models.SET_NULL, null=True, blank=True, related_name='head_of_household')
    
    def __str__(self):
        return self.household_name


class Resident(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    CIVIL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthdate = models.DateField()
    address = models.CharField(max_length=255, null=False, default='Unknown')
    household = models.ForeignKey('Household', on_delete=models.SET_NULL, null=True, blank=True)
    events  = models.ManyToManyField('BarangayEvent', related_name='residents', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("res_detail", kwargs={"pk": self.pk})


class Official(models.Model):
    position = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    term_start = models.DateField()
    term_end = models.DateField()
    resident = models.OneToOneField('Resident', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.position}: {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("official_detail", kwargs={"pk": self.pk})

class BarangayEvent(models.Model):
    event_name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    overseen_by = models.ForeignKey(Official, on_delete=models.SET_NULL, null=True, blank=True, related_name='events')

    def __str__(self):
        return self.event_name

class IncidentReport(models.Model):
    title = models.CharField(max_length=200)
    report_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    reported_by = models.ForeignKey('Resident', on_delete=models.SET_NULL, null=True, related_name='reported_incidents')
    involved_residents = models.ManyToManyField('Resident', related_name='incidents_involved')
    events = models.ManyToManyField('BarangayEvent', related_name='incidents', blank=True)  # Many-to-Many field
    

    def __str__(self):
        return self.title  
