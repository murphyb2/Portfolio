from django.shortcuts import render
from PortfolioApp.models import Image

def index(request):
    """View function for home page of site."""

    #context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

# Create your views here.
