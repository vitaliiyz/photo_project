from django.urls import path
from home.views import home, about

urlpatterns = [path("", home, name="home_page"), path("about/", about, name="about_page")]
