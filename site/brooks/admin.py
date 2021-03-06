#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Arcovid-19 Brooks.
# Copyright (c) 2020, Juan B Cabral, Vanessa Daza, Diego García Lambas,
#                     Marcelo Lares, Nadia Luczywo, Dante Paz, Rodrigo Quiroga,
#                     Bruno Sanchez, Federico Stasyszyn.
# License: BSD-3-Clause
#   Full Text: https://github.com/ivco19/brooks/blob/master/LICENSE


# =============================================================================
# IMPORTS
# =============================================================================

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models as mdls


# =============================================================================
# TITLE
# =============================================================================

admin.site.site_header = _('Brooks Admin')

admin.site.site_title = _('Brooks Admin')

admin.site.index_title = _('Brooks Admin')


# =============================================================================
# USERS
# =============================================================================

class UserProfileInline(admin.StackedInline):
    verbose_name_plural = "Profile"
    model = mdls.UserProfile


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
