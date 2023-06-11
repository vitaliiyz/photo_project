from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import ContactForm


def contact(request):
    cform = ContactForm()
    if request.method == "POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            messages.info(request, "Completed :)")
            return redirect("contact_page")
    return render(request, "contact.html", {"cform": cform, "page_tag": "contact"})
