from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QuestionManager(models.Manager):                                          
    def new(self):                                                              
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM mybase
            ORDER BY added_at DESC""")
        return cursor.fetchone()
    def popular():                                                          
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM mybase
            ORDER BY rating DESC""")
        return cursor.fetchone()

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User, related_name='user_likes')
    class Meta:
        db_table = 'question'
        
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User, related_name='user')
    class Meta:
        db_table = 'answer'