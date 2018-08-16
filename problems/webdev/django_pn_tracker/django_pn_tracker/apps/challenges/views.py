from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


########################################
# Fill in all ###s in the views below. #
# Uncomment the funcs when complete.   #
########################################

# def challenge_list(request):
#     template_name = ###
#     attendees =  ###
#     context = ###

#     return render(request, template_name, context=context)


# def challenge_add(request):
#     template_name = ###
#     form = forms.AttendeeEditForm()
#     #############################################
#     # Logic for capturing submitted information #
#     #############################################
#     context = {"form": form}

#     return render(request, template_name, context=context)


# def challenge_edit(request, id):
#     attendee = get_object_or_404(models.AttendeeInfo, id=id)
#     template_name = ###
#     form = ###
#     #############################
#     # Logic for capturing edits #
#     #############################
#     context = {"form": form}

#     return render(request, template_name, context=context)


# def challenge_delete(request, id):
#     attendee = ###
#     template_name = ###
#     form = ###
#     ######################################
#     # Logic for capturing delete request #
#     ######################################
#     context = ###

#     return ###
