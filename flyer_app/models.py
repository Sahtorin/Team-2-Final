from django.db import models
from django.contrib.auth.models import User


#DONE
class Profile(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    display_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    profile_link = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name
    
#Flyer model still needs finished.
class Flyer(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=50)
    flyer_name = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50, blank=True)
    event_date = models.DateField()
    event_location = models.CharField(max_length=100)
    cover_charge = models.DecimalField()

    def __str__(self):
        return self.flyer_name
