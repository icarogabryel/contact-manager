from django.views.generic import ListView

from contacts.models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'
