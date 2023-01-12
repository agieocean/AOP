from django.contrib import admin

from .models import AOPCoreAbuser, AOPCoreReport, AOPCoreWorkPlace

class AbuserAdmin(admin.ModelAdmin):
    search_fields = ["sid", "name"]
    list_display = ("name", "sid", "approved")

class AOPReportAdmin(admin.ModelAdmin):
    search_fields = ["sid"]
    list_display = ("abuserName", "sid", "approved")
class WorkPlaceAdmin(admin.ModelAdmin):
    search_fields = ["sid"]
    list_display = ("name", "sid", "approved")

admin.site.register(AOPCoreAbuser.Abuser, AbuserAdmin)
admin.site.register(AOPCoreReport.AOPReport, AOPReportAdmin)
admin.site.register(AOPCoreWorkPlace.WorkPlace, WorkPlaceAdmin)