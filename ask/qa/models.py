from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QuestionQuerySet(models.QuerySet):
    def new(self):
        return self.order_by("-id")

    def popular(self):
        return self.order_by("-rating")

class QuestionManager(models.Manager):    
    def get_queryset(self):
        return QuestionQuerySet(self.model, using=self._db)     

    def new(self):
        return self.get_queryset().new()

    def popular(self):
        return self.get_queryset().popular()

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='user_likes')

    def __str__(self):
        return self.title
        
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
