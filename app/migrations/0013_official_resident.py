# Generated by Django 5.0.3 on 2024-11-30 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_incidentreport_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='official',
            name='resident',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.resident'),
        ),
    ]
