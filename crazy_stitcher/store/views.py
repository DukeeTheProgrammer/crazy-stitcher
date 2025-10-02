from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.auth.models import User
from .models import Category, Product, Review

# Create your views here.

def home(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    return render(request, "store/index.html", {"product":product, "categories":categories})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = formed.cleaned_data["email"]
            password = form.cleaned_data["password"]

            #save the user
            User.object.create_user(
                    username=name,
                    email=email,
                    password=password
                    )
            return HttpResponse(f"{name} has been registered successfully")
    else:
        form = SignupForm()
        return render(request, "signup.html", {"form":form})


def category(request):
    categories = Category.objects.all()
    return render(request, "store/category.html", {"categories":categories})

def product(request):
    products = Product.objects.all()
    return render(request, "store/product.html",{"products":products} )

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return HttpResponse("Not Available Right Now.")

def services(request):
    return HttpResponse("Not Available Right Now.")

def category_detail(request, category_name):
    category = Category.objects.filter(name=category_name).first()
    product = Product.objects.filter(category=category.id).all()
    return render(request, "store/category_details.html", {"category":category})

def products_in_category(request, cat_name):
    cat = Category.objects.filter(name=cat_name).first()
    products = Product.objects.filter(category=cat.id).all()
    return render(request, "store/products.html", {"products":products})

def buy_product(request, cat_name, id):
    p = Product.objects.filter(id=id,name=cat_name).first()
    path = request.build_absolute_uri()
    return render(request, "store/buy.html" , {"path":path, "p":p})

def review(request):
    reviews = Review.objects.all()
    return render(request, "store/reviews.html", {"reviews":reviews})

def add_review(request):
    if request.method == "POST":
        username = request.POST.get("username")
        review_text = request.POST.get("review")
        Review.objects.create(
                username=username,
                review=review_text
                )
        return redirect('review')

    return render(request, "store/add_review.html")

