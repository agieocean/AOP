from django.db import models
from django.forms import ModelForm
import django as dj
from django.db.models.signals import post_save
from django.dispatch import receiver
import intake.utils
import uuid

# Create your models here.
class WorkPlace(models.Model):
    class Meta:
        app_label = "intake"
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    sid = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name
@receiver(post_save, sender=WorkPlace)
def queue_task(sender, instance, created, **kwargs):
    if instance.approved:
        intake.utils.uploadb()
class WorkPlaceForm(ModelForm):
    class Meta:
        model = WorkPlace
        fields = ["name", "location"]