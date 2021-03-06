# Generated by Django 3.0.4 on 2020-04-17 08:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import ingest.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RawFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('file', models.FileField(upload_to=ingest.models._raw_file_upload_to, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv', 'xlsx'])], verbose_name='archivo')),
                ('notes', models.TextField(blank=True, verbose_name='notas')),
                ('merged', models.BooleanField(default=False, verbose_name='integrado')),
                ('size', models.IntegerField(null=True)),
                ('broken', models.BooleanField(default=False, verbose_name='Roto')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raw_files', to=settings.AUTH_USER_MODEL, verbose_name='creado por')),
                ('modify_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raw_files_modified', to=settings.AUTH_USER_MODEL, verbose_name='modificado por')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
