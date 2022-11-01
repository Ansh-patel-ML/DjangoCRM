from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect

from leads.forms import LeadForm, LeadModelForm
from .models import Agent, Lead
# Create your views here.

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads/")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            lead.first_name = form.cleaned_data['first_name']
            lead.last_name = form.cleaned_data['last_name']
            lead.age = form.cleaned_data['age']
            lead.agent = form.cleaned_data['agent']
            lead.save()
            return redirect(f"/leads/{pk}")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads/")