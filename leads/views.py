from django.shortcuts import reverse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView
from django.core.mail import send_mail
from leads.forms import LeadModelForm, CustomUserCreationForm
from .models import Lead


class SignUpView(CreateView):
    template_name: str = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


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

    def form_valid(self, form):
        send_mail (
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="patelansh883@gmail.com",
            recipient_list=["pansh7529@fmail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(UpdateView):
    template_name: str = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")

class LeadDeleteView(DeleteView):
    template_name: str = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

