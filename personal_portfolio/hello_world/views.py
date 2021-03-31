from .forms import RegisterForm, LoginForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserUniqueToken
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group, User

title = 'lol'
value = 'invalueable'
# Create your views here.

def default_page(request):
    return redirect('front/login')

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():


            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data.get('password1')
            # user = User.objects.create_user(
            #     username = username,
            #     email = email,
            #     password = raw_password,
            #     first_name = first_name
            # )

            user = form.save()            
            group = Group.objects.get(name='vendor')

            user.groups.add(group)
            user.is_active = False
            user.save()
            import uuid
            print(uuid.uuid4().hex)
            UserUniqueToken.objects.create(user_id=user, token = uuid.uuid4().hex)
            return redirect('/front/register-success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'singlepage/register.html', {'form': form})


def register_success(request):
    link = None
    return render(request, 'singlepage/info.html', {'message': 'Silahkan cek email anda untuk melakukan verifikasi akun.', 'link':link})


def register_verification(request, tokenurl=None, uuid=None):
    from datetime import date
    import hashlib
    link = None

    usertoken = UserUniqueToken.objects.filter(token=tokenurl)
    if usertoken.exists():
        uid = usertoken[0].user_id_id
        user = User.objects.filter(id=uid)
        if user.exists():
            if not user[0].is_active:
                userencode = hashlib.md5(
                    user[0].username.encode('utf-8')).hexdigest()
                if userencode == uuid and usertoken[0].datetime <= date.today(): #broken
                    user = user[0]
                    user.is_active = True
                    user.save()
                    return render(request, 'singlepage/verification-success.html')
                else:
                    return render(request, 'singlepage/info.html', {'message': 'Link verifikasi telah kadaluwarsa', 'link': link})
            else:
                return redirect('/vendor/data-vendor')
        else:
            return render(request, 'singlepage/info.html', {'message': 'User tidak ditemukan', 'link': link})
    else:
        return render(request, 'singlepage/info.html', {'message': 'User tidak ditemukan', 'link': link})
            

# def loginVendor(request):
#     print(request)
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = LoginForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:

#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/front/register-success')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = LoginForm()

#     return render(request, 'singlepage/login.html', {'form': form})


def loginVendor(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/vendor/data-vendor')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'singlepage/login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        user = User.objects.get(username=request.POST["username"])
        print(user)
        if user is not None:
            if not user.is_active:
                #######################
                import hashlib
                userencode = hashlib.md5(user.username.encode('utf-8')).hexdigest()
                usertoken = UserUniqueToken.objects.get(user_id_id=user.id)
                token = usertoken.token
                link = token+'/'+userencode
                #######################
                return render(request, 'singlepage/info.html', {'message': 'Silahkan cek email anda untuk melakukan verifikasi akun.', 'link':link})
            else:
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return HttpResponseRedirect('/vendor/data-vendor')
                    
                else:
                    # If there were errors, we render the form with these
                    # errors
                    return render(request, 'singlepage/login.html', {'form': form})
        else:
            print('User not found')


def logoutVendor(request):
    logout(request)
    return redirect('login')


def testpage(request, tokenurl=None, uuid=None):
    from datetime import date
    import hashlib

    usertoken = UserUniqueToken.objects.filter(token=tokenurl)
    if usertoken.exists():
        uid = usertoken[0].user_id_id
        user = User.objects.filter(id=uid)
        if user.exists():
            userencode = hashlib.md5(user[0].username.encode('utf-8')).hexdigest()
            if userencode == uuid and usertoken[0].datetime <= date.today():
                user = user[0]
                user.is_active = True
                user.save()


    return render(request, 'testpage.html', {'user' : user})
