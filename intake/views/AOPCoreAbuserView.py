from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .. import urls
from ..models import AOPCoreAbuser
from ..models import AOPCoreWorkPlace
import uuid

def abuser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AOPCoreAbuser.AbuserForm(request.POST)
        if not form.data["workplace"]:
            if not form.data["workplace_choice"]:
                form.fields["workplace_choice"].queryset = AOPCoreWorkPlace.WorkPlace.objects.filter(approved__in=[True])
                return render(request, 'aopcore/abuser.html', {'form': form, 'alert': "A workplace needs to be entered"})
        # check whether it's valid:
        if form.is_valid():
            m = form.save()
            m.approved = False
            if form.data["workplace_choice"]:
                m.workplace = str(form.cleaned_data["workplace_chhoice"])
            m.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            m = form.save()
            return render(request, 'thanks.html', {'sid': m.sid})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AOPCoreAbuser.AbuserForm()
        form.fields["workplace_choice"].queryset = AOPCoreWorkPlace.WorkPlace.objects.filter(approved__in=[True])
    return render(request, 'aopcore/abuser.html', {'form': form})
