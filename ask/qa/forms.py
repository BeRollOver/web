from django import forms
from django.forms import ModelForm
from .models import Question, Answer
from django.forms import widgets

class AskForm(forms.ModelForm): 
    class Meta:
        model = Question
        fields = ['title', 'text', 'author']
        widgets = {
            'author': widgets.HiddenInput(),
        }

class AnswerForm(forms.ModelForm): 
    class Meta:
        model = Answer
        fields = ['text', 'question', 'author']
        widgets = {
            'question': widgets.HiddenInput(),
            'author': widgets.HiddenInput(),
        }