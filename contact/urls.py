from django.urls import path
from contact.views import contact, get_in_touch

urlpatterns = [path("", contact, name="contact_page"), path("get_in_touch/", get_in_touch, name="get_in_touch_page")]
