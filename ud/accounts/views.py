from django.shortcuts import redirect,render
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        password2 = request.POST['password']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'that username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'that email is taken')
                    return redirect('register')
                else:
                    # looks good
                    user= User.objects.create_user(username=username, password = password, email =email, first_name = first_name, last_name = last_name)
                    #auth.login(request, user)
                    #messages.success(request, 'you are now looged in')
                    #return redirect('index')
                    user.save()
                    messages.success(request, 'you are now logged in')
                    return redirect('login')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')
    else:

        return render(request, 'accounts/register.html')
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, ' you are not logged in ')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'accounts/logout.html')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

