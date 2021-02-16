from django.urls import path
from . import views


urlpatterns = [
    path('' , views.quizHome , name = 'quizHome'),
    path('startQuiz/' , views.startQuiz , name = 'startquiz'),
    path('question/<int:quesid>/' , views.showQues, name = 'nextQuestion' )
]