from django.urls import reverse_lazy
from django.views import generic

from contacts.models import Contact


class ContactListView(generic.ListView):
    model = Contact
    template_name = 'contact-list.html'
    context_object_name = 'contacts'


class ContactDetailView(generic.DetailView):
    model = Contact
    template_name = 'contact-detail.html'
    context_object_name = 'contact'


class ContactCreateView(generic.CreateView):
    model = Contact
    template_name = 'contact-form.html'
    success_url = reverse_lazy('contact-list')
    fields = '__all__'


class ContactUpdateView(generic.UpdateView):
    model = Contact
    template_name = 'contact-form.html'
    success_url = reverse_lazy('contact-list')
    fields = '__all__'


class ContactDeleteView(generic.DeleteView):
    model = Contact
    template_name = 'contact-delete.html'
    success_url = reverse_lazy('contact-list')