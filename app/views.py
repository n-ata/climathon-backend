from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Blogs

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def logout_view(request):
    auth.logout(request)
    return redirect('index')

def register_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password = request.POST['password']

        if not username or not password:
            return render(request, 'app/register.html', {'error': 'Please enter all required fields.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'app/register.html', {'error': 'Username already exists.'})
        if password != password1:
            return render(request, 'app/register.html', {'error': 'Passwords are not same.'})


        user = User.objects.create(
            username=username,
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
        user.set_password(password)
        user.save()

        auth.login(request, user)
        return redirect('app:index')
    else:
        return render(request, 'app/register.html')
    
def index(request):
    return render(request, 'app/index.html')

def create_post_view(request):
    if request.method == 'POST':
        user = request.user
        image = request.FILES['image']
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        Blogs.objects.create(title=title, image=image, text=description, user=user)
        return render(request, 'app/create-post.html')
    else:
        return render(request, 'app/create-post.html')