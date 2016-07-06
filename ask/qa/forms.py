from django import forms
from django.forms import ModelForm
from .models import Question, Answer

class AskForm(ModelForm): 
    class Meta:
        model = Question
        fields = ['title', 'text']

    def clean(self):
        return self.instance.cleaned_data

class AnswerForm(ModelForm): 
    class Meta:
        model = Answer
        fields = ['text', 'question']
