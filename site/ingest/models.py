#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Arcovid-19 Brooks.
# Copyright (c) 2020, Juan B Cabral, Vanessa Daza, Diego García Lambas,
#                     Marcelo Lares, Nadia Luczywo, Dante Paz, Rodrigo Quiroga,
#                     Bruno Sanchez, Federico Stasyszyn.
# License: BSD-3-Clause
#   Full Text: https://github.com/ivco19/brooks/blob/master/LICENSE


# =============================================================================
# DOCS
# =============================================================================

"""Static models for the ingest app."""


# =============================================================================
# IMPORTS
# =============================================================================

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
from django_extensions.db.models import TimeStampedModel

from ingest.libs import mdesc


# =============================================================================
# RAW FILE UPLOAD
# =============================================================================

def _raw_file_upload_to(instance, filename):
    folder = instance.created.strftime("%Y_%m")
    return '/'.join(["raw_files", folder, filename])


class RawFile(TimeStampedModel):

    DATA_FILE_EXTENSIONS = [e[1:] for e in mdesc.DATA_FILE_EXTENSIONS]

    file = models.FileField(
        upload_to=_raw_file_upload_to,
        validators=[
            FileExtensionValidator(allowed_extensions=DATA_FILE_EXTENSIONS)],
        verbose_name="archivo")

    notes = models.TextField(blank=True, verbose_name="notas")
    merged = models.BooleanField(default=False, verbose_name="integrado")
    size = models.IntegerField(null=True)

    broken = models.BooleanField(
        default=False, verbose_name="Roto")

    created_by = models.ForeignKey(
        User, related_name="raw_files",
        on_delete=models.CASCADE, verbose_name="creado por")
    modify_by = models.ForeignKey(
        User, related_name="raw_files_modified",
        on_delete=models.CASCADE, verbose_name="modificado por")

    @property
    def is_parsed(self):
        return bool(self.generated.count())

    @property
    def filename(self):
        return self.file.url.rsplit("/", 1)[-1]
