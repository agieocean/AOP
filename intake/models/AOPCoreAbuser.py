from django.db import models
from django.forms import ModelForm
import django as dj
from django.db.models.signals import post_save
from django.dispatch import receiver
import boto3
import json
import uuid
import intake.utils
from .AOPCoreWorkPlace import WorkPlace
    
# Create your models here.
class Abuser(models.Model):
    class Meta:
        app_label = "intake"
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    workplace = models.CharField(max_length=200, blank=True)
    workplace_choice = models.ForeignKey(WorkPlace, blank=True, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField(blank=True)
    picture = models.URLField(blank=True)
    badgeOr = models.CharField(max_length=50, blank=True)
    approved = models.BooleanField(default=False)
    sid = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name


@receiver(post_save, sender=Abuser)
def queue_task(sender, instance, created, **kwargs):
    if instance.approved:
        intake.utils.uploadb()

class AbuserForm(ModelForm):
    class Meta:
        model = Abuser
        fields = ["name", "occupation", "workplace", "workplace_choice", "age", "picture", "badgeOr"]