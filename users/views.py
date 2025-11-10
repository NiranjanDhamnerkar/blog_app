from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm  we comment this because we create forms.py and add this line to that file
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm , profileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request , f'Your Account Created Succefully {username}! Log In Now!!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request , 'users/register.html' , {'form':form})


# login require decorater for profile route(url)
@login_required # if we go url and type profile now it give error page because user not log in. we handle this error page to route to login page simply in settings.py we need to define LOGIN_URL = 'login'  (login is the the our login page name we assign in views.py) if user go to without login in url section and type profile now it goes to login page.
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance= request.user)
        p_form = profileUpdateForm (request.POST , request.FILES , instance= request.user.profile)

        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request , f'Your Account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = profileUpdateForm (instance= request.user.profile)

    context = {
      'u_form' : u_form,
      'p_form' : p_form
    }

    return render(request , 'users/profile.html' , context)



