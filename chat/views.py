from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

@login_required
def index(request):
    return render(request, 'chat/index.html', {'username': request.user.username})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # Automatically log them in
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

# YOUR NEW LOGIN VIEW
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) # Securely log the user in
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

# YOUR NEW LOGOUT VIEW
def logout(request):
    auth_logout(request) # Securely destroy the session
    return redirect('login') # Send them back to the login page


from django.http import JsonResponse
from .models import Message

@login_required
def room_history(request, room_name):
    # Get the last 50 messages for this room
    messages = Message.objects.filter(room_name=room_name).order_by('timestamp')[:50]
    
    # Package them into a list
    history = []
    for msg in messages:
        history.append({
            'id': msg.id,
            'username': msg.user.username,
            'content': msg.content,
            'image_url': msg.image_url,
            'timestamp': msg.timestamp.isoformat()
        })
    return JsonResponse(history, safe=False)