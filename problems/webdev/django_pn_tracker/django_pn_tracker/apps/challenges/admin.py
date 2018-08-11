from django.contrib import admin
from . import models


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


admin.site.register(models.ChallengeTools) 
admin.site.register(models.Challenge, ChallengeAdmin) 
admin.site.register(models.AttendeeInfo)
