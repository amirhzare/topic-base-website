from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

def editRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # Get the cleaned data (values) from the form
            form_values = form.cleaned_data

            room.host = form_values['host']
            room.topic = form_values['topic']
            room.name = form_values['name']
            room.description = form_values['description']
            room.save()
            return redirect('home')
            
        else:
            print("Form is not valid. Please check for errors.")
    context = {'form': form}
    return render(request, 'base/edit.html', context)