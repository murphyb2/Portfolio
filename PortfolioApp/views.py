from django.shortcuts import render
from PortfolioApp.models import Image, Home

def index(request):
    """View function for home page of site."""
    title = Home.title.__str__
    img_gal = Home.image_gallery.all()
    context = {
        'title': title,
        'img_gal': img_gal,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)


