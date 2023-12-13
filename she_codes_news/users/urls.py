from django.urls import path
from .views import CreateAccountView
from .views import AuthorProfileView
from .views import UpdateProfileView

app_name = 'users'

urlpatterns = [
      path('create-account/', CreateAccountView.as_view(), name='createAccount'),
      path('author-profile/', AuthorProfileView.as_view(), name='authorProfile'),
      path('update-profile/', UpdateProfileView.as_view(), name='updateProfile'),
]