from django.shortcuts import render, redirect


def contact(request):
    return render(request, "contact.html", {"page_tag": "contact"})


def get_in_touch(request):
    if request.method == "POST":
        data = request.POST
        print(dict(data))
    return redirect("contact_page")
