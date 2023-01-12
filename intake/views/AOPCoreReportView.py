from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .. import urls
from ..models import AOPCoreReport, AOPCoreAbuser, AOPCoreWorkPlace
import uuid

def report(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AOPCoreReport.AOPReportForm(request.POST)
        # check whether it's valid:
        #print("waga baba bobo")
        #print(form.errors)
        if not form.data["workplace"]:
            if not form.data["workplaceChoice"]:
                form.fields["workplaceChoice"].queryset = AOPCoreWorkPlace.WorkPlace.objects.filter(approved__in=[True])
                form.fields["abuserChoice"].queryset = AOPCoreAbuser.Abuser.objects.filter(approved__in=[True])
                return render(request, 'aopcore/report.html', {'form': form, 'alert': "A workplace needs to be entered"})
        if not form.data["abuserName"]:
            if not form.data["abuserChoice"]:
                form.fields["workplaceChoice"].queryset = AOPCoreWorkPlace.WorkPlace.objects.filter(approved__in=[True])
                form.fields["abuserChoice"].queryset = AOPCoreAbuser.Abuser.objects.filter(approved__in=[True])
                return render(request, 'aopcore/report.html', {'form': form, 'alert': "An abuser needs to be entered"})
        
        if form.is_valid():
            m = form.save()
            m.approved = False
            if form.data["workplaceChoice"]:
                m.workplace = str(form.cleaned_data["workplaceChoice"])
            if form.data["abuserChoice"]:
                m.abuserName = str(form.cleaned_data["abuserChoice"])
            m.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'thanks.html', {'sid': m.sid})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AOPCoreReport.AOPReportForm()
        form.fields["workplaceChoice"].queryset = AOPCoreWorkPlace.WorkPlace.objects.filter(approved__in=[True])
        form.fields["abuserChoice"].queryset = AOPCoreAbuser.Abuser.objects.filter(approved__in=[True])

    return render(request, 'aopcore/report.html', {'form': form})