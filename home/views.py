from django.shortcuts import render

# Create your views here.
def display_items():
    ...

def home(request):
    return render(request, "home/home.html")