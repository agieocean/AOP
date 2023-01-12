#import boto3
import json, os, datetime
from django.apps import apps
#from botocore.config import Config
#from .models import AOPCoreAbuser, AOPCoreReport, AOPCoreWorkPlace
from b2sdk.v2 import *

info = InMemoryAccountInfo()

b2_api = B2Api(info)

application_key_id = ''

application_key = ''

b2_api.authorize_account("production", application_key_id, application_key)

def uploadb():
    data = {}
    AOPCoreAbuser = apps.get_model('intake.Abuser')
    AOPCoreReport = apps.get_model('intake.AOPReport')
    AOPCoreWorkPlace = apps.get_model('intake.WorkPlace')
    abusersOb = AOPCoreAbuser.objects.filter(approved__in=[True])
    data["abusers"] = list(AOPCoreAbuser.objects.filter(approved__in=[True]).values())
    for it, abuser in enumerate(data["abusers"]):
        data["abusers"][it]["sid"] = str(data["abusers"][it]["sid"])
        if data["abusers"][it]["workplace_choice_id"] != None:
            data["abusers"][it]["workplace_choice_id"] = str(abusersOb[it].workplace_choice.sid)
    reportsOb = AOPCoreReport.objects.filter(approved__in=[True])
    data["reports"] = list(AOPCoreReport.objects.filter(approved__in=[True]).values())
    reportsrm = []
    for it, report in enumerate(data["reports"]):
        reportf = report
        reportf.pop("contactEmail", None)
        reportf["dateOf"] = str(report["dateOf"])
        reportf["sid"] = str(report["sid"])
        if data["reports"][it]["abuserChoice_id"] != None:
            print(reportsOb[it])
            data["reports"][it]["abuserChoice_id"] = str(reportsOb[it].abuserChoice.sid)
        if data["reports"][it]["workplaceChoice_id"] != None:
            data["reports"][it]["workplaceChoice_id"] = str(reportsOb[it].workplaceChoice.sid)
        reportsrm.append(reportf)
    data["reports"] = reportsrm
    data["workplaces"] = list(AOPCoreWorkPlace.objects.filter(approved__in=[True]).values())
    for it, abuser in enumerate(data["workplaces"]):
        data["workplaces"][it]["sid"] = str(data["workplaces"][it]["sid"])
    with open("currentdb.json", "w") as f:
        f.write(json.dumps(data))
    #s3.Bucket("aop-bucket").upload_file("currentdb.json", "currentdb.json")
    bucket = b2_api.get_bucket_by_name("aop-bucket")
    bucket.upload_local_file(
        local_file="currentdb.json",
        file_name="currentdb.json"
    )
    # B2 version keeps all versions of the file so this is not necessary, however, it may be necessary on other systems
    #fname = "db-{0}.json".format(datetime.datetime.now().strftime("%m/%d/%Y-%H:%M:%S"))
    """bucket.upload_local_file(
        local_file="currentdb.json",
        file_name=fname
    )"""