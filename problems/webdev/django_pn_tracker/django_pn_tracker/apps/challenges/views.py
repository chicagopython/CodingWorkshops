from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def challenge_list(request):
    template_name = "challenges/list.html"

    attendees =  models.AttendeeInfo.objects.all()

    context = {"attendees": attendees}
    return render(request, template_name, context=context)


def challenge_add(request):
    template_name = "challenges/edit.html"
    form = forms.AttendeeEditForm()
    if request.method == 'POST':
        form = forms.AttendeeEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("challenges_list")
    context = {"form": form}
    return render(request, template_name, context=context)


def challenge_edit(request, id):
    attendee = get_object_or_404(models.AttendeeInfo, id=id)
    template_name = "challenges/edit.html"
    form = forms.AttendeeEditForm(instance=attendee)
    if request.method == 'POST':
        form = forms.AttendeeEditForm(instance=attendee, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("challenges_list")
    context = {"form": form}
    return render(request, template_name, context=context)


def challenge_delete(request, id):
    attendee = get_object_or_404(models.AttendeeInfo, id=id)
    template_name = "challenges/delete.html"
    form = forms.ConfirmForm()
    if request.method == 'POST':
        form = forms.ConfirmForm(request.POST)
        if form.is_valid():
            attendee.delete()
            return redirect("challenges_list")
    context = {"form": form}
    return render(request, template_name, context=context)
