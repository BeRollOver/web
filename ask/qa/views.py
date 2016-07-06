from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from qa.models import Question
from django.core.paginator import Paginator
from .forms import AskForm, AnswerForm

# Create your views here.
from django.http import HttpResponse

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm()
    return render(request, 'qa/detail.html', {'question': question, 'form': form})

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(form.save().get_url())

    else:
        form = AskForm()

    return render(request, 'qa/question_details.html', {'form': form})

    
def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect(form.save().get_url())
    else:
        return HttpResponseRedirect('/')

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