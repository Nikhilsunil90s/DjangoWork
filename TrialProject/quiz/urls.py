from django.urls import path
from . import views
from .views import QuestionView

urlpatterns = [
    path('' , views.quizHome , name = 'quizHome'),
    path('startQuiz/' , QuestionView.as_view() , name = 'startquiz'),
    #path()
]