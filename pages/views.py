from django.shortcuts import render
from pages.forms import ContactForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from pages.models import Contact

def home(request):
    context = RequestContext(request)
    return render(request, 'index.html', context)

def contact(request):
    context = RequestContext(request)
    context['form'] = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            place = form.cleaned_data['place']
            new_contact = Contact(name=name, email=email, place=place)
            new_contact.save()
            return HttpResponseRedirect('/thanks/')

    return render(request, 'contact.html', context)