from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Flyer, Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "display_name",
            "profile_image",
            "bio",
            "profile_link",
        )


class FlyerForm(forms.ModelForm):
    class Meta:
        model = Flyer
        fields = (
            "artist_name",
            "flyer_name",
            "event_name",
            "event_date",
            "event_location",
            "cover_charge",
            "event_link",
            "flyer_image",
            "background_color",
            "font_color",
            "font_family",
        )

        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}),
        }
