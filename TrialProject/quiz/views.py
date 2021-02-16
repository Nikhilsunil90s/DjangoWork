from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.
nextHits = 1

def quizHome(request):
    return render(request , 'quiz/quizhome.html')


def startQuiz(request):
    global nextHits
    print(nextHits)
    nextHits += 1
    results = Question.objects.all()
    choices = Choice.objects.get(ques = results[0].quesId)
    print(choices.choice_1)
    return render(request , 'quiz/quizpage.html' , {'FirstQuestion' : results[0] , 'QuesChoices' : choices , 'nextHits' : nextHits})

def showQues(request , quesid):
    global nextHits
    print(nextHits)
    nextHits += 1
    quest = Question.objects.get(quesId = quesid)
    questChoice = Choice.objects.get(ques = quesid)
    #return HttpResponse("<h1>" + str(quesid) + " : " + str(ques) + "</h1>")
    return render(request , 'quiz/quizpage.html' , {'NextQuestion' : quest , 'QuesChoices' : questChoice , 'nextHits' : nextHits})