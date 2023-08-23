from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomLoginForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .backends import EmailBackend


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Utiliza el backend personalizado para autenticar
            user = authenticate(request, username=username, password=password, backend=EmailBackend)

            if user is not None:
                login(request, user)
                return redirect('home')  # Reemplaza 'home' con la URL a la que deseas redirigir
            else:
                messages.error(request, 'Credenciales incorrectas. Inténtalo nuevamente.')
    else:
        form = CustomLoginForm()
    
    context['form'] = form
    context['title'] = 'Iniciar sesión'

    return render(request, 'accounts/base.html', context)



def register_view(request):
    context = {}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            return redirect('home')
    else:
        form = CustomUserCreationForm()

    context['form'] = form
    context['title']= 'Registrarse'

    return render(request, 'accounts/base.html', context)