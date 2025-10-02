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
        path("category_detail/<str:category_name>", views.category_detail,name="category_detail"),
        path("product_in_category/<str:cat_name>", views.products_in_category, name="products_in_category"),
        path("buy_product/<str:cat_name>/<int:id>",views.buy_product, name="buy_product"),
        path("review/",views.review,name="review"),
        path("add-review/", views.add_review, name="add_review"),
        ]
