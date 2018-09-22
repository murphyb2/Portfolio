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
    # ADD VALIDATION TO ENSURE THAT ASPECT RATIO IS 3x2 or 2x3 IF USING AS A HOME PAGE SHOWCASE IMAGE!!!!! 
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', height_field='height', width_field='width', null=True)
    image_url = models.CharField(blank=True, null=True, max_length=200)
    # thumbnail_url = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=200, null=True)
    #priority = models.IntegerField(default=0)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    #portfolio_section = models.ManyToManyField(PortfolioSection, on_delete=models.CASCADE)
    is_showcase_image = models.BooleanField(default=False)

    def __str__(self):
        return self.alt_text

    def is_landscape(self):
        return self.width > self.height

class Home(models.Model):
    # Model representing the home page

    # Array holding the showcase clickable images to link to each portfolio section
    # showcase_images = []

    title = models.CharField(default="Home", max_length=100)
    # title = "home"

    def __str__(self):
        return self.title