from django.shortcuts import render
from django.http import HttpResponse


# Views based on functions (FBV)
def home_1(request):
    return HttpResponse("<h1>Bienvenidos a Tienda Libre</h1>")

def home(request):
    return render(request, 'ecommerce/index.html', {})