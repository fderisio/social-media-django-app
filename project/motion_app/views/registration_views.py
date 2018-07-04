from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from project.motion_app.models import UserForm


class SignUpView(FormView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('overview')
    form_class = UserForm

    def signup(self, request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('name')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('overview')
        else:
            form = UserForm()
        return render(request, 'registration/signup.html', {'form': form})

    # def form_valid(self, form):
    #     User.objects.create(
    #         name=form.cleaned_data.get('name'),
    #         email=form.cleaned_data.get('email'),
    #         password=form.cleaned_data.get('password'),
    #     )
    #     return super().form_valid(form)

    #     if request.method == 'POST':
    #         form = UserForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             username = form.cleaned_data.get('name')
    #             raw_password = form.cleaned_data.get('password1')
    #             user = authenticate(username=username, password=raw_password)
    #             login(request, user)
    #             return redirect('overview')
    #     else:
    #         form = UserForm()
    #     return render(request, 'registration/signup.html', {'form': form})
