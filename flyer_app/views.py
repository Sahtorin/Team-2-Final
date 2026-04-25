from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .forms import FlyerForm, ProfileForm, RegisterForm
from .models import Flyer, Profile

#render home.html with flyers from db.
def home(request):
    flyers = Flyer.objects.select_related("profile").all()[:6]
    return render(request, "flyer_app/home.html", {"flyers": flyers})

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
    profile = get_object_or_404(Profile, user=request.user)
    flyers = Flyer.objects.filter(profile=profile)
    return render(request, "flyer_app/dashboard.html", {
        "profile": profile,
        "flyers": flyers,
    })

@login_required
def profile_detail(request):
    # get current user's profile
    # render profile_detail.html with profile
    pass


@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_detail")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "flyer_app/profile_edit.html", {"form": form})


@login_required
def flyer_list(request):
    profile = get_object_or_404(Profile, user=request.user)
    flyers = Flyer.objects.filter(profile=profile)

    return render(request, "flyer_app/flyer_list.html", {
        "flyers": flyers,
    })

def flyer_detail(request, pk):
    flyer = get_object_or_404(Flyer.objects.select_related("profile"), pk=pk)
    return render(request, "flyer_app/flyer_detail.html", {"flyer": flyer})

@login_required
def flyer_create(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = FlyerForm(request.POST, request.FILES)
        if form.is_valid():
            flyer = form.save(commit=False)
            flyer.profile = profile
            flyer.save()
            return redirect("flyer_detail", pk=flyer.pk)
    else:
        form = FlyerForm()

    return render(request, "flyer_app/flyer_form.html", {
        "form": form,
        "page_title": "Create Flyer",
    })


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
    profile = get_object_or_404(Profile, user=request.user)

    flyer = get_object_or_404(Flyer, pk=pk, profile=profile)

    if request.method == "POST":
        flyer.delete()
        return redirect("flyer_list")

    return render(request, "flyer_app/flyer_confirm_delete.html", {
        "flyer": flyer,
    })