from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class DateModelBase(models.Model):
    # Learn about model fields:
    # https://docs.djangoproject.com/en/2.1/ref/models/fields/
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        # Learn about abstract base classes:
        # https://docs.djangoproject.com/en/2.1/topics/db/models/#abstract-base-classes
        abstract = True


class ChallengeTools(DateModelBase, models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        # learn about django model Meta options:
        # https://docs.djangoproject.com/en/2.1/ref/models/options/
        verbose_name = "Challenge Tool"
        verbose_name_plural = "Challenge Tools"


class Challenge(DateModelBase, models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    tools = models.ManyToManyField("challenges.ChallengeTools", blank=True)

    def __str__(self):
        return f"{self.name}"


########################################
# Fill in all ###s in the model below. #
# Uncomment the class when complete.   #
########################################

# class AttendeeInfo(###, ###):
#     date = ###
#     name = ###
#     challenge = ###(###, on_delete=models.CASCADE)
#     skills = ###
#
#     def __str__(self):
#         return f"{self.challenge} {self.name}"
