from django.shortcuts import render, redirect
from django.contrib import messages


def contact(request):
    return render(request, "contact.html", {"page_tag": "contact"})


def get_in_touch(request):
    if request.method == "POST":
        data = request.POST
        print(dict(data))
        messages.info(request, "Completed :)")
    return redirect("contact_page")
