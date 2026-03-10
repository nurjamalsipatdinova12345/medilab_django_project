
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
def signup_view(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        u_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=u_name).exists():
            return render(request, 'signup.html', {'error': 'Bu username aldin qoyilgan'})
        user = User.objects.create_user(username=u_name, email=email, password=password)
        user.first_name = f_name
        user.last_name = l_name
        user.save()

        return redirect('login')

    return render(request, 'signup.html')
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('doctor_view')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('doctor_view')
