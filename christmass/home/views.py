from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import NameForm
# Create your views here.


def message(request, username):
    user = CustomUser.objects.get(username=username)

    return render(request, 'message.html', {'user': user})


def index(request):
    form = NameForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            username = f"{first_name.capitalize()} {last_name.lower()}"

            user = CustomUser.objects.create_user(
                username=username, password=None)

            user.first_name = first_name
            user.last_name = last_name

            user.save()

            return redirect('message', username=username)
        else:
            form = NameForm()
    return render(request, 'index.html', {'form': form})
