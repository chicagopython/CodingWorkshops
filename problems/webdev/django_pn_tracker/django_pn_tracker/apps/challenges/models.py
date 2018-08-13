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


class AttendeeInfo(DateModelBase, models.Model):
    date = models.DateTimeField()
    name = models.CharField("Participant Name", max_length=128)
    challenge = models.ForeignKey(
        "challenges.Challenge", on_delete=models.CASCADE)
    skills = models.IntegerField(
        default=1,
        # Learn about validators:
        # https://docs.djangoproject.com/en/2.1/ref/validators/
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f"{self.challenge} {self.name}"
