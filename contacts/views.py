from django.views.generic import ListView, DetailView

from contacts.models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = 'contact-list.html'
    context_object_name = 'contacts'


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact-detail.html'
    context_object_name = 'contact'