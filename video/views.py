
# Create your views here.
# chat/views.py
from django.shortcuts import render


def main_view(request):
    context = {}
    return render(request, "video/index.html")

def room(request, room_name):
    return render(request, "video/room.html", {"room_name": room_name})