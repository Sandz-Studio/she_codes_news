from django.urls import path
from . import views
from .views import UpdateStoryView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('update-story/<int:pk>/', views.UpdateStoryView.as_view(), name='updateStory'),
    path('delete-story/<int:story_id>/', views.DeleteStoryView.as_view(), name='deleteStory')
]
