from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path("contact/",views.contact,name="contact-page"),
    path("zoom/",views.zoom,name="zoom-page"),
    path("about/",views.about,name="about-page"),
]
