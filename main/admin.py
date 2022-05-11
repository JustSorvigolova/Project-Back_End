from django.contrib import admin

from . import models

admin.site.register(models.Projects)
admin.site.register(models.Tasks)
admin.site.register(models.Comments)