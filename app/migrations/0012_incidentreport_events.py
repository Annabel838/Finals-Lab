# Generated by Django 5.0.3 on 2024-11-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_barangayevent_overseen_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentreport',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='incidents', to='app.barangayevent'),
        ),
    ]
