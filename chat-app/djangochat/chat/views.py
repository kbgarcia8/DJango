from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username') #gets the variable username in your link
    room_details = Room.objects.get(name=room) #will get the particular model that has the room name
    return render(request,'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

"""to check if room and username exist in database
if the room does exist it will not duplicate but
will redirect you to it"""
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else: 
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
        
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
#get messges of a room
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    #get all the details with the room id that contains the room_details.id
    return JsonResponse({"messages":list(messages.values())})