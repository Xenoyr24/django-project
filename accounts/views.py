from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.utils.http import is_safe_url
from accounts.models import Profile 



from .forms import LoginForm, RegisterForm, GuestForm

from .models import GuestEmail
from django.contrib.auth.decorators import login_required



from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from accounts.forms import UserForm,ProfileForm

from accounts.models import Profile

from django.contrib import messages


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email    = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")

def logout_page(request):
        logout(request)
        return redirect("/login")


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
           print("Error")
    return render(request, "accounts/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
         "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        
        messages.success(request, f'Your account has been created! You are now able to log in')
        return redirect('/login')
    else:
        pass
    return render(request, "accounts/register.html", context) 

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        pass_form = PasswordChangeForm(data=request.POST, user=request.user)
        #profile = Profile.objects.get_or_create(user=request.user)
        if user_form.is_valid() and profile_form.is_valid() and pass_form.is_valid():
            user_form.save()
            profile_form.save()
            pass_form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'Your profile was successfully updated!')
            return redirect("/profile/edit/")
        else:
            pass
    else:
         profile_form = ProfileForm()

        
         user_form = UserForm(instance=request.user)
         profile_form = ProfileForm(instance=request.user.profile)
         pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/edit_profile.html', { 'user_form': user_form, 'profile_form': profile_form, 'pass_form': pass_form })

    #    context = {
   #     'u_form': u_form,
   #     'p_form': p_form









#@login_required
#def edit_profile(request):
#    if request.method == 'POST':
#        form = EditProfileForm(request.POST, instance=request.user)
#        if form.is_valid():
#           form.save()
#          return render(request,'accounts/profile.html',{})
# else:
#    formedit = EditProfileForm(instance=request.user)
#   context = {'form': formedit}
#  return render(request, 'accounts/edit_profile.html', context)