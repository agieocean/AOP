from django.db import models
from django.forms import ModelForm
import django as dj
import intake.models.AOPCoreAbuser as AOPCoreAbuser
from django.db.models.signals import post_save
from django.dispatch import receiver
import intake.utils
import uuid
from .AOPCoreAbuser import Abuser
from .AOPCoreWorkPlace import WorkPlace

# Create your models here.
class AOPReport(models.Model):
    class Meta:
        app_label = "intake"
    #abuser = models.ForeignKey(AOPCoreAbuser.Abuser, on_delete=models.DO_NOTHING)
    abuserName = models.CharField(max_length=200, blank=True)
    abuserChoice = models.ForeignKey(Abuser, blank=True, on_delete=models.SET_NULL, null=True)
    workplace = models.CharField(max_length=200, blank=True)
    workplaceChoice = models.ForeignKey(WorkPlace, blank=True, on_delete=models.SET_NULL, null=True)
    fullText = models.CharField(max_length=2000)
    typeOf = models.CharField(max_length=50)
    dateOf = models.DateField()
    ongoing = models.BooleanField(default=False)
    helpRequested = models.BooleanField(default=False)
    typeHelpRequested = models.CharField(default="", max_length=100, blank=True)
    helpComment = models.CharField(default="", max_length=1000, blank=True)
    contactEmail = models.EmailField(default="", blank=True)
    donationDetails = models.CharField(default="", max_length=500, blank=True)
    approved = models.BooleanField(default=False)
    sid = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.abuserName
@receiver(post_save, sender=AOPReport)
def queue_task(sender, instance, created, **kwargs):
    if instance.approved:
        intake.utils.uploadb()
class AOPReportForm(ModelForm):
    class Meta:
        model = AOPReport
        widgets = {
            'fullText': dj.forms.Textarea(attrs={'class': 'field'})
        }
        fields = [
            "abuserName",
            "abuserChoice",
            "workplace",
            "workplaceChoice",
            "fullText",
            "typeOf",
            "dateOf",
            "ongoing",
            "helpRequested",
            "typeHelpRequested",
            "helpComment",
            "contactEmail",
            "donationDetails"
        ]