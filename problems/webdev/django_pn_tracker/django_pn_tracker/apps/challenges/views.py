from django.shortcuts import render
from . import models


def challenge_list(request):
    template_name = "challenges/list.html"

    attendees =  models.AttendeeInfo.objects.all()

    context = {"attendees": attendees}
    return render(request, template_name, context=context)