from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from contacts.models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = 'contact-list.html'
    context_object_name = 'contacts'


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact-detail.html'
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contact-form.html'
    success_url = reverse_lazy('contact-list')
    fields = '__all__'
