from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from .models import Question, Answer, Like
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Question, Answer, Like
from django.contrib.auth import logout 
# View to display all questions
class QuestionListView(ListView):
    model = Question
    template_name = 'registration/question_list.html'
    context_object_name = 'questions'



# View to post a question
class QuestionCreateView(CreateView):
    model = Question
    template_name = 'registration/question_form.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('question_list')

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'registration/question_form.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# View to display a specific question and its answers
class QuestionDetailView(UpdateView):
    model = Question
    template_name = 'registration/question_detail.html'
    fields = ['title', 'body']

# View to answer a question
class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    template_name = 'registration/answer_form.html'
    fields = ['body']
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

# View to like an answer
class LikeView(LoginRequiredMixin, CreateView):
    model = Like

    def post(self, request, *args, **kwargs):
        answer_id = self.kwargs['answer_id']
        like = Like(answer_id=answer_id, user=request.user)
        like.save()
        return redirect('question_list')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('question_list')



def love(request):
    return HttpResponse('hello')

class Profile(TemplateView):
    template_name='registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        context['users'] = users  
        return context
