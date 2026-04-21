from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    display_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    profile_link = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_name"]

    def __str__(self):
        return self.display_name
    

class Flyer(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="flyers")
    artist_name = models.CharField(max_length=50)
    flyer_name = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50, blank=True)
    event_date = models.DateField()
    event_location = models.CharField(max_length=100)
    cover_charge = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    event_link = models.URLField(blank=True)
    flyer_image = models.ImageField(upload_to="flyers/", blank=True, null=True)
    background_color = models.CharField(max_length=20, default="#000000")
    font_color = models.CharField(max_length=20, default="#FFFFFF")
    font_family = models.CharField(max_length=50, default="Arial")
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["event_date", "flyer_name"]

    def __str__(self):
        return self.flyer_name
