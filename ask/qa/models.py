from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QuestionManager(models.Manager):    
    def new(self):
        return self.order_by("-id")

    def popular(self):
        return self.order_by("-rating")

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1)
    likes = models.ManyToManyField(User, related_name='user_likes')

    def __str__(self):
        return self.title

    def get_url(self):
        return '/question/{0}/'.format(self.pk)
        
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default=1)

    def get_url(self):
        return '/question/{0}/'.format(self.question.pk)
