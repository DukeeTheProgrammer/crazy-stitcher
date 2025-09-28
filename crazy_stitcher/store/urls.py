from . import views
from django.urls import path


urlpatterns = [
        path("home/", views.home, name="home"),
        path("signup/", views.signup, name="signup"),
        path("category/", views.category, name="category"),
        path("about/", views.about, name="about"),
        path("product/", views.product, name="product"),
        path("contact/", views.contact, name="contact"),
        path("services/", views.services, name="services"),
        ]
