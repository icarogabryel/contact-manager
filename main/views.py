from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all()

    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')

    return render(request, 'contact_create.html', {'form': ContactForm()})
