from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View

from .models import Comment
from .forms import CommentForm, RegisterForm


class IndexView(View):
    template_name = 'home/index.html'
    model = Comment
    form_control = CommentForm

    def get_queryset(self):
        return self.model.objects.all().order_by('pk')

    def get_context_data(self, **kwargs):
        context = {}
        context['commentaries'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('home:index')
        else:
            messages.error(request, 'Usuario o contraseña no son validos')
    return render(request, 'home/login_or_create.html', {

    })


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('home:index')
    return render(request, 'home/login_or_create.html', {
        'form': form,
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('home:index')
