from django.shortcuts import render

# Create your views here.
def display_items():
    ...

def display_user(request):
    return render(request, "home/userpage.html")

def home(request):
    return render(request, "home/home.html")