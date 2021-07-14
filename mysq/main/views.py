from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import LoginForm, RegistrationForm, DotsForm
from .models import Dots


def main(request):

    error = ''
    if request.method == 'POST':
        form = DotsForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            x = form.cleaned_data['x_value']
            y = form.cleaned_data['y_value']
            r = float(form.cleaned_data['r_value'])
            flag = False
            if (x >= 0) and (y <= 0) and (x <= r) and (y >= r/2):
                flag = True
            elif (x < 0) and (y <= 0) and (y >= -(x+r)):
                flag = True
            elif (x > 0) and (y > 0) and (x**2 + y**2 <= r**2):
                flag = True
            new_form.result = flag
            new_form.save()
        else:
            error = 'Вы ввели неверные значения'

    form = DotsForm()
    dots = Dots.objects.order_by('-id')
    data = {
        'form': form,
        'error': error,
        'dots': dots
    }

    return render(request, 'main/main.html', data)


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}
        return render(request, 'main/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'main/login.html', context)


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'main/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')

        context = {'form': form}
        return render(request, 'main/registration.html', context)