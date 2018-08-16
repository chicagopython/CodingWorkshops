from django.contrib import admin
from . import models

# Learn about the Django Admin:
# https://docs.djangoproject.com/en/2.1/ref/contrib/admin/
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


admin.site.register(models.ChallengeTools)
admin.site.register(models.Challenge, ChallengeAdmin)

##############################
# Register AttendeeInfo here #
##############################