from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from qa.models import Question
from django.core.paginator import Paginator
from .forms import AskForm, AnswerForm

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
import random
import datetime

def signup(request):
    error = '' 
    if request.method == 'POST': 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password, email=email).save()
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        return HttpResponseRedirect('/')

    return render(request, 'registration/signup.html', {'error': error })

def login(request):
    error = '' 
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        url = request.POST.get('continue', '/') 
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Redirect to a success page.
                response = HttpResponseRedirect('/')
                response.set_cookie('sessionid', str(random.randrange(1000000)),  
                    httponly=True, 
	                expires = datetime.datetime.now()+datetime.timedelta(days=5) 
                )
                return response
            else:
                # Return a 'disabled account' error message
                error = 'disabled account'
        else:
            # Return an 'invalid login' error message.
            error = 'invalid login'

    return render(request, 'registration/login.html', {'error': error }) 


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if(request.user.is_authenticated()):
        form = AnswerForm(initial={'question': question})
    else:
        form = AnswerForm(initial={'question': question, 'author': request.user})
    return render(request, 'qa/detail.html', {'question': question, 'form': form})

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(form.save().get_url())

    else:
        if(request.user.is_authenticated()):
            form = AskForm(initial={'author': request.user})
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