from django.shortcuts import render, redirect, HttpResponse
from accounts.forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.user.is_authenticated:
        return redirect('blog:article_list')

    # todo: create decorator only not login
    # todo: redirect user in profile

    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                messages.success(request, f"{request.user.username},Login Successfully")
                return redirect('accounts:profile')
            else:
                messages.error(request, 'phone or password is wrong', 'warning')
    else:
        form = LoginUserForm()

    return render(request, 'accounts/login.html', context={'form': form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('blog:article_list')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = get_user_model().objects.create(
                username=cd['username'], password=cd['password'], email=cd['email']
            )

            login(request=request, user=new_user)
            messages.success(request, f"{request.user.username},Login Successfully", 'success')
            return redirect('accounts:profile')

    else:
        form = RegisterUserForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'you are Logout', 'success')
    return redirect('accounts:login')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
