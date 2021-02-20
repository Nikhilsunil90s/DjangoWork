from django.db import models

# Create your models here.

class Question(models.Model):
    quesId = models.IntegerField(primary_key=True)
    quesTitle = models.CharField(max_length=200)
    quesDescription = models.CharField(max_length=200)
    quesCreatedOn = models.DateTimeField()

    def __str__(self):
        return self.quesTitle

    

class Choice(models.Model):
    ques = models.ForeignKey('Question' , on_delete = models.CASCADE)
    choice_1 = models.CharField(max_length=100)
    choice_2 = models.CharField(max_length=100)
    choice_3 = models.CharField(max_length=100)
    choice_4 = models.CharField(max_length=100)
    correctChoice = models.CharField(max_length=100)




