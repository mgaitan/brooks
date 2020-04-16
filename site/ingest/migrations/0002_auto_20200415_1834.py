# Generated by Django 3.0.4 on 2020-04-15 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ingest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated', to=settings.AUTH_USER_MODEL, verbose_name='Creado por'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='raw_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated', to='ingest.RawFile', verbose_name='Archivo'),
        ),
    ]