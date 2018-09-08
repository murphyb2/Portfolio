from django.db import models


""" class HomePage(models.Model):
    # Model representing a page on the home interface
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

class PortfolioSection(models.Model):
    # Model representing a page containing a section of the portfolio
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title """

class Image(models.Model):
    # Model representing an image file contained in a portfolio section
    image_url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=200, blank=True)
    #priority = models.IntegerField(default=0)
    width = models.IntegerField()
    height = models.IntegerField()
    #portfolio_section = models.ManyToManyField(PortfolioSection, on_delete=models.CASCADE)

    def __str__(self):
        return self.alt_text

    def is_landscape(self):
        return self.width > self.height

