from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User
from app_two import forms

# Create your views here.

def index(request):
    return HttpResponse('Hello There. Go to /help for help page. Go to /users for User page. Go to /signup for signup!')


def help(request):
    my_dict = {"help_temp":"Help Page"}
    return render(request, "app_two/app_two.html", context = my_dict)

def users(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'users':user_list}
    return render(request,'app_two/user.html',context=user_dict)

def signup(request):
    f = forms.UserForm()

    if request.method == 'POST':
        f = forms.UserForm(request.POST)

        if f.is_valid():
            f.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')

    return render(request,'app_two/signup.html', {'form1':f})
