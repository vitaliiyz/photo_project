from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required(login_url="/account/login/")
def contact(request):
    cform = ContactForm()
    if request.method == "POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            cform.save()
            messages.info(request, "Completed :)")
            return redirect("contact_page")
    return render(request, "contact.html", {"cform": cform, "page_tag": "contact"})
