from django.shortcuts import render, redirect #redirect is to redirect to /<link/path>
from django.http import HttpResponse
from django.contrib.auth.models import User, auth 
#User is the default database of user in /admin, auth is function of method to authenticate
from django.contrib import messages
#Used to display message if you have an error or just display imagge
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})
"""in your html substitute the variables just like what was done during URL routing 
Just like how you print in html"""

def register(request):
    #get inputted data on your html
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                #This is where the imported from django.contrib import messages is used
                return redirect('register') #redirect to the link /register
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                """The username, email and password called at variable user are declared and has a
                value of the username, email and password that has the request.POST['<var_name>']"""
                user.save();
                return redirect('login')
        else:
                messages.info(request, 'Password does not match')
                return redirect('register')
    else:
        return render(request, 'register.html')
#Login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = auth.authenticate(username=username, password=password)
    
        if user is not None:
            auth.login(request, user)
            return redirect('/') #redirect to home page
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

#Logout
def logout(request):
    auth.logout(request)
    return redirect('/') #back to home page

def counter(request):
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
    return render(request, 'counter.html', {'posts': posts})

"""from index.html the inputted text is obtained from action="counter" then will be passed to the "words" variable in def(counter)
after above process the data will be put (when printed/called) to counter.html by assigning a key to the 
value word count obtained by len function """

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})