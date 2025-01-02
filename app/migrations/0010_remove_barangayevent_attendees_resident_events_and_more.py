# Generated by Django 5.0.3 on 2024-11-27 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_incidentreport_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barangayevent',
            name='attendees',
        ),
        migrations.AddField(
            model_name='resident',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='residents', to='app.barangayevent'),
        ),
        migrations.AlterField(
            model_name='barangayevent',
            name='event_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='barangayevent',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='household',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='head_of_household', to='app.resident'),
        ),
        migrations.AlterField(
            model_name='household',
            name='household_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='resident',
            name='address',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='resident',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='resident',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resident',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='resident',
            name='household',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.household'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
