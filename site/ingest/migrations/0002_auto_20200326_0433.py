# Generated by Django 3.0.4 on 2020-03-26 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='ingest.Hospital', verbose_name='Centro de salud'),
        ),
        migrations.AddField(
            model_name='event',
            name='infection_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='ingest.InfectionSource', verbose_name='F. de Infección'),
        ),
        migrations.AddField(
            model_name='event',
            name='travel_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='ingest.TravelFrom', verbose_name='Origen'),
        ),
    ]
