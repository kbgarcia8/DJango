from django.shortcuts import render
from .models import Posts #import the class from models.py

# Create your views here.
def index(request):
    posts = Posts.objects.all() #access all objects from models.py created through the database
    return render(request, 'index.html', {'posts': posts}) #create 'key': value pair

def post(request, counter):
    posts = Posts.objects.get(id=counter) #get the objects associated with id number of the database entry
    return render(request, 'posts.html', {'posts': posts})