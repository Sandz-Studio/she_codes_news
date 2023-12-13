from typing import Any
from django.db import models
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory, Comment
from .forms import StoryForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from users.models import CustomUser
from .forms import CommentForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['form'] = CommentForm()
        return context

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdateStoryView(generic.UpdateView):
    model = NewsStory
    template_name = 'news/updateStory.html'
    fields = ['title', 'category', 'image', 'content']

    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk': self.object.pk})
    
    # stop someone going through url to update a story that is not theirs
    def form_valid(self, form):
        if form.instance.author == self.request.user:
            return super().form_valid(form)

# Function based view to confirm delete success
# def DeleteSuccessView(request):
#     return render(request, 'news/deleteSuccess.html')

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')
    context_object_name = 'deletestory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = NewsStory.objects.get(id=self.kwargs['pk'])
        return context

class ViewAuthorView(generic.DetailView):
    model = CustomUser
    template_name = 'news/viewAuthor.html'
    context_object_name = 'viewAuthor'

    def get_object(self, *args, **kwargs):
        return CustomUser.objects.get(pk=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_id = self.kwargs['pk']

        # get the author's stories
        context['all_stories'] = NewsStory.objects.filter(author_id=author_id)
        context['author'] = CustomUser.objects.get(id=self.kwargs['pk'])
        return context
    
class AddCommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'news/story.html'
    context_object_name = 'comments'

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk"))

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        response = super().form_valid(form)
        return response
    
    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('news:story', kwargs={'pk': pk})

# If i have time do delete comment view

# class DeleteCommentView(generic.DeleteView):
#     model = Comment
#     template_name = 'news/story.html'
#     # success_url = reverse_lazy('news:index')
#     context_object_name = 'deletecomment'
