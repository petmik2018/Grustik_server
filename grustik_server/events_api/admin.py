from django.contrib import admin

from events_api import models

# Register your models here.

admin.site.register(models.Event)
admin.site.register(models.EventUser)

