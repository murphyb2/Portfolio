from django.shortcuts import render
from PortfolioApp.models import Image

def index(request):
    """View function for home page of site."""

    # Filter all the images in the database for only those that are assigned to 
    # the Home section and that are showcase images. 
    img_gal = Image.objects.filter(portfolio_section='Home')
    img_gal = Image.objects.filter(is_showcase_image=True)
    
    context = {
        'title': 'Home',
        'img_gal': img_gal,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)


def colorFilm(request):
    """View function for Color Film page of site."""

    # Filter all the images in the database for only those that are assigned to 
    # the Color Film section. 
    img_gal = Image.objects.filter(portfolio_section='35mm color')
    
    context = {
        'title': 'Color Film',
        'img_gal': img_gal,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)