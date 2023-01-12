from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .. import urls
from ..models import AOPCoreWorkPlace
import uuid

def workplace(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AOPCoreWorkPlace.WorkPlaceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            m = form.save()
            m.approved = False
            m.save()
            return render(request, 'thanks.html', {'sid': m.sid})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AOPCoreWorkPlace.WorkPlaceForm()

    return render(request, 'aopcore/workplace.html', {'form': form})