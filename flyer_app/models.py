from django.db import models
from django.contrib.auth.models import User

#needs to flesh out with fields. Just the model Structures right now.

#Profile model
#profile_image
#display_name
#bio
#profle_link
#created
#last_upadted

class Profile(models.Model):

    def __str__(self):
        return self.display_name
    
#Flyer model
class Flyer(models.Model):

    def __str__(self):
        return self.flyer_name
