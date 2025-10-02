# views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')  # Cambia 'home' por el nombre de tu URL de destino

    def form_valid(self, form):
        # Guarda el usuario y haz login automáticamente
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())