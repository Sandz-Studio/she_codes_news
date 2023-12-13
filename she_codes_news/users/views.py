from typing import Any
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic

from news.models import NewsStory
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class AuthorProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/authorProfile.html'
    context_object_name = 'authorprofile'

    def get_object(self, *args, **kwargs):
        return self.request.user
    
    # getting all user stories
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.request.user).order_by('-pub_date')
        return context
    
class UpdateProfileView(generic.UpdateView):
    model = CustomUser
    template_name = 'users/updateProfile.html'
    fields = ['first_name', 'last_name', 'birth_date','username', 'email', 'profile_photo', 'bio']

    def get_object(self, *args, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:authorProfile')

# If have time have a view to delete profile