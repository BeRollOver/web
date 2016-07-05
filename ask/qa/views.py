from django.shortcuts import render, get_object_or_404
from django.http import Http404
from qa.models import Question
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse
def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/detail.html', {'question': question})

def index(request):
    try:
        page=request.GET.get('page', 1)
    except ValueError:
        raise Http404
    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    try: 
        page = paginator.page(page)
    except EmptyPage: 
        page = paginator.page(paginator.num_pages) 
    return render(request, 'qa/index.html', {
        'questions':  page.object_list,
        'paginator':  paginator,
        'page':    page,
    })

def popular(request):
    try:
        page=request.GET.get('page', 1)
    except ValueError:
        raise Http404
    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/popular/?page='
    try: 
        page = paginator.page(page)
    except EmptyPage: 
        page = paginator.page(paginator.num_pages) 
    return render(request, 'qa/index.html', {
        'questions':  page.object_list,
        'paginator':  paginator,
        'page':    page,
    })