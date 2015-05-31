from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic

from . import models as mymodels

# Create your views here.from django.http import HttpResponse


def index(request):
    model= mymodels.Patient

def clindate(request, clindate):
    (year, month, day) = clindate.split("-")

    return HttpResponse("Clinic date %s" % year+" "+month+" "+day)


class DetailView(generic.DetailView):
    model = mymodels.Patient
    template_name = 'pttrack/patient.html'

def intake(request):
    from . import forms as myforms

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = myforms.PatientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            p = mymodels.Patient(**form.cleaned_data)
            p.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse("patient", args=(p.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = myforms.PatientForm()

    return render(request, 'pttrack/intake.html', {'form': form})
