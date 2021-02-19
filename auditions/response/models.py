from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    ques_round = models.IntegerField(default=1)
    types = [
        ('N','NORMAL'),
        ('I','IMAGE')
    ]
    question_type = models.CharField(max_length=1,choices=types)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'media/images',blank=True)

    def __str__(self):
        return str(self.ques_round)

class Response(models.Model):
    question = models.OneToOneField(Question,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    response = models.TextField()

    def __str__(self):
        return "{} : {}".format(self.question.ques_round,self.user.first_name+self.user.last_name)


