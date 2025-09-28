from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, "store/index.html")

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
    return render(request, "store/category.html")

def product(request):
    return render(request, "store/product.html")

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return HttpResponse("Not Available Right Now.")

def services(request):
    return HttpResponse("Not Available Right Now.")
