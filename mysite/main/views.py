from django.shortcuts import render
from main.forms import UserForm, UserProfileForm, ContactForm
# for log in and out functionalities:
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'insert':'Hello World!'})



def fancy_forms(request):
    form = ContactForm()
    return render(request, 'main/fancy.html', {'form':form})


def register(request):
    registered = False
    user_form = UserForm()
    profile_form = UserProfileForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)


    return render(request, 'main/register.html', {'user':user_form,
                                                  'profile':profile_form,
                                                  'registered':registered})


# don't call your view login to avoid conflict with the built-in function
def user_login(request):

    if request.method == 'POST':
        # cuz we named username input in html so from that post we'll get the user name submitted
        username = request.POST.get('username')
        password = request.POST.get('password')

        # specify the args here to make it clear to django
        # then the function will authenticate the user
        user = authenticate(username=username, password=password)

        # means if user exists(if it's been authenticated)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account Not Active!')

        else:
            print('someone tried to login and failed!')
            print(f'Username: {username}, password: {password}')
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request, 'main/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse('You are logged in Yay!!!')
