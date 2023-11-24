from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')
def message(request):
    if request.method == 'POST':
        sender = request.POST['name']
        if sender is not None:
            user = User.objects.create_user(username=sender)
            user.save()
            return render(request,'message.html')
    else:
        return render(request,'index.html')
