from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView

from leads.forms import LeadModelForm
from .models import Lead

class LandingPageView(TemplateView):
    template_name: str = "landing.html"


class LeadListView(ListView):
    template_name: str = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name: str = "leads"

class LeadDetailView(DetailView):
    template_name: str = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name: str = "lead"

class LeadCreateView(CreateView):
    template_name: str = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse("leads:lead-list")

class LeadUpdateView(UpdateView):
    template_name: str = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")

class LeadDeleteView(DeleteView):
    template_name: str = "leads/lead_delete.html"
