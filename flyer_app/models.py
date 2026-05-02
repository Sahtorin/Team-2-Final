from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )
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
    BACKGROUND_COLOR_CHOICES = [
        ("#2b241f", "Worn"),
        ("#e2dfd7", "Bone"),
        ("#f1a512", "Cheese"),
        ("#dd4111", "Rust"),
        ("#8c0027", "Oxblood"),
        ("#2baf90", "Island"),
        ("#a1d4b1", "Sage"),
    ]

    FONT_COLOR_CHOICES = [
        ("#2b241f", "Worn"),
        ("#e2dfd7", "Bone"),
        ("#f1a512", "Cheese"),
        ("#dd4111", "Rust"),
        ("#8c0027", "Oxblood"),
        ("#2baf90", "Island"),
        ("#a1d4b1", "Sage"),
    ]

    FONT_FAMILY_CHOICES = [
        ("'Bebas Neue', sans-serif", "Default"),
        ("'Climate Crisis', sans-serif", "Heavy"),
        ("Crushed, sans-serif", "Retro"),
        ("Lobster, cursive", "Script"),
        ("'Playwrite NO', cursive", "Written"),
        ("'Playwrite NZ Guides', cursive", "Sketched"),
        ("'Syne Mono', monospace", "Type"),
        ("'Unica One', sans-serif", "Poster"),
    ]

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="flyers"
    )
    artist_name = models.CharField(max_length=50)
    flyer_name = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50, blank=True)
    event_date = models.DateField()
    event_location = models.CharField(max_length=100)
    cover_charge = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    event_link = models.URLField(blank=True)
    flyer_image = models.ImageField(upload_to="flyers/", blank=True, null=True)

    background_color = models.CharField(
        max_length=20, choices=BACKGROUND_COLOR_CHOICES, default="#e2dfd7"
    )

    font_color = models.CharField(
        max_length=20, choices=FONT_COLOR_CHOICES, default="#2b241f"
    )

    font_family = models.CharField(
        max_length=50, choices=FONT_FAMILY_CHOICES, default="Bebas Neue"
    )

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["event_date", "flyer_name"]

    def __str__(self):
        return self.flyer_name
