from django.contrib import admin

from .forms import StoryForm
from .models import NewsStory

# Add these depending on if I do these models
# Category, Comment

admin.site.register(NewsStory)
# admin.site.register(Category)
# admin.site.register(Comment)
