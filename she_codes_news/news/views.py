from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.shortcuts import render
from users.models import CustomUser

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

def DeleteSuccessView(request):
    return render(request, 'news/deleteSuccess.html')

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


 