from datetime import date
from decimal import Decimal
from django.contrib.auth.models import User
from django.test import TestCase
from .forms import FlyerForm, ProfileForm, RegisterForm
from .models import Profile, Flyer


class ModelTests(TestCase):
    def test_profile_and_flyer_workflow(self):
        user = User.objects.create_user(username="josh", password="GoodPass123!")
        profile = Profile.objects.create(user=user, display_name="Joshua")

        flyer = Flyer.objects.create(
            profile=profile,
            artist_name="The Devil Makes Three",
            flyer_name="Friday Night Show",
            event_name="Live at The Coterie",
            event_date=date(2026, 5, 1),
            event_location="The Coterie",
            cover_charge=Decimal("10.00"),
        )

        self.assertEqual(str(profile), "Joshua")
        self.assertEqual(str(flyer), "Friday Night Show")
        self.assertEqual(flyer.profile, profile)
        self.assertEqual(profile.flyers.count(), 1)

    def test_delete_user_cascades_to_profile_and_flyers(self):
        user = User.objects.create_user(username="josh", password="GoodPass123!")
        profile = Profile.objects.create(user=user, display_name="Joshua")
        flyer = Flyer.objects.create(
            profile=profile,
            artist_name="The Devil Makes Three",
            flyer_name="Friday Night Show",
            event_name="Live at The Coterie",
            event_date=date(2026, 5, 1),
            event_location="The Coterie",
            cover_charge=Decimal("10.00"),
        )

        profile_id = profile.id
        flyer_id = flyer.id

        user.delete()

        self.assertFalse(Profile.objects.filter(id=profile_id).exists())
        self.assertFalse(Flyer.objects.filter(id=flyer_id).exists())


class RegisterFormTests(TestCase):
    def test_register_form_valid_data(self):
        form = RegisterForm(data={
            "username": "josh",
            "email": "josh@example.com",
            "password1": "GoodPass123!",
            "password2": "GoodPass123!",
        })

        self.assertTrue(form.is_valid())

    def test_register_form_requires_matching_passwords(self):
        form = RegisterForm(data={
            "username": "josh",
            "email": "josh@example.com",
            "password1": "GoodPass123!",
            "password2": "BadPass123!",
        })

        self.assertFalse(form.is_valid())


class ProfileFormTests(TestCase):
    def test_profile_form_valid_data(self):
        form = ProfileForm(data={
            "display_name": "Joshua",
            "bio": "I'm making a backend",
            "profile_link": "https://google.com",
        })

        self.assertTrue(form.is_valid())


class FlyerFormTests(TestCase):
    def test_flyer_form_valid_data(self):
        form = FlyerForm(data={
            "artist_name": "The Devil Makes Three",
            "flyer_name": "Friday Night Show",
            "event_name": "Live at The Coterie",
            "event_date": "2026-05-01",
            "event_location": "The Coterie",
            "cover_charge": "10.00",
        })

        self.assertTrue(form.is_valid())

    def test_flyer_form_requires_required_fields(self):
        form = FlyerForm(data={
            "artist_name": "",
            "flyer_name": "",
            "event_date": "",
            "event_location": "",
        })

        self.assertFalse(form.is_valid())