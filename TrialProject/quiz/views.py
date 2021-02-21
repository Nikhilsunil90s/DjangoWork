from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice
from django.core.paginator import Paginator
from django.views.generic.list import ListView
# Create your views here.

class QuestionView(ListView):
    model = Question
    template_name = 'question_list.html'
    paginate_by = 1
    context_object_name = 'QuestionContext'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(Question.objects.all(), self.paginate_by)
        page = self.request.GET.get('page')
        #print(self.request.build_absolute_uri())
        #pp = paginator.page(page)
        if page:
            context['Choices'] = Choice.objects.get(ques = page)
            context['result'] = ''
        else:
            context['Choices'] = Choice.objects.get(ques = Question.objects.all()[0].quesId)
            context['result'] = ''
        return context



def quizHome(request):
    return render(request , 'quiz/quizhome.html')


