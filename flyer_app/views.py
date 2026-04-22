from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .forms import FlyerForm, ProfileForm, RegisterForm
from .models import Flyer, Profile

#if logged in go to dashboard, or go to login
def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")

#signup/register with redirect
def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)

        #saves Django User
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()

            #makes matching profile, default profile display_name to User username
            Profile.objects.get_or_create(
                user=user,
                defaults ={"display_name": user.username},
            )

            #login immediately and redirects
            login(request,user)
            return redirect("dashboard")
    #if not POST, makes blank form, render register.html
    else:
        form = RegisterForm()
    return render(request, "flyer_app/register.html", {"form": form})

@login_required
def dashboard(request):
    # get current user's profile
    # get that user's flyers
    # render dashboard.html with profile and flyers
    pass


@login_required
def profile_detail(request):
    # get current user's profile
    # render profile_detail.html with profile
    pass


@login_required
def profile_edit(request):
    # get current user's profile

    # if POST:
        # build edit form
        # save if valid
        # redirect to profile page
    # else:
        # show prefilled form

    # render profile_edit.html with form
    pass


@login_required
def flyer_list(request):
    # get current user's profile
    # get that user's flyers
    # render flyer_list.html with flyers
    pass


@login_required
def flyer_detail(request, pk):
    # get flyer by pk for current user
    # render flyer_detail.html with flyer
    pass


@login_required
def flyer_create(request):
    # get current user's profile

    # if POST:
        # build flyer form
        # if valid, finish flyer and save it
        # redirect to flyer detail
    # else:
        # show blank flyer form

    # render flyer_form.html with form and page title
    pass


@login_required
def flyer_edit(request, pk):
    # get flyer by pk for current user

    # if POST:
        # build edit form for flyer
        # save if valid
        # redirect to flyer detail
    # else:
        # show prefilled flyer form

    # render flyer_form.html with form and page title
    pass


@login_required
def flyer_delete(request, pk):
    # get flyer by pk for current user

    # if POST:
        # delete flyer
        # redirect to flyer list

    # render flyer_confirm_delete.html with flyer
    pass