from django.db import models


class DateModelBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ChallengeTools(DateModelBase, models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
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
    skills = models.IntegerField(default=0)  # TODO validate to 1-10

    def __str__(self):
        return f"{self.challenge} {self.name}"
