from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Question,Person
from django.utils import timezone
from django.contrib import messages
# Create your views here.

def profile(request):
    person = Person.objects.get(username=request.user.username)
    return render(request,'profile.html',{'person':person,'profile':True})

def profile_update(request):
    person = Person.objects.get(username=request.user.username)
    return render(request,'form.html',{'person':person})

def profile_update_action(request):
    if request.method=='POST':
        person = Person.objects.get(username=request.user.username)
        if len(request.POST)==0:
            return render(request,'profile.html',{'person':person,'profile':True})
        else:
            if not request.POST['name']=='':
                person.name = request.POST['name']
            if not request.POST['age']=='':
                person.age = request.POST['age']
            if not request.POST['mobno']=='':
                person.mobile_no = request.POST['mobno']
            person.save()
            return render(request,'profile.html',{'person':person,'profile':True})
    return render(request,'form.html',{'person':''})

def home(request):
    if request.user.is_authenticated:
        person = Person.objects.get(username=request.user.username)
        return render(request,'home.html',{'person':person,'home':True})
    return render(request,'home.html')


def input(request):
    if request.method == 'POST':
        if request.POST['temp']=='':
            messages.info(request,'Enter the temperature for sure..!')
            return render(request,'enter.html',{'enter':True})
        if ('temp') in request.POST:
            temperature = request.POST['temp']
        else:
            temperature = 36
        current_symptoms=''
        previous_diseases=''
        if ('cough') in request.POST:
            current_symptoms += 'cough '
        if ('fever') in request.POST:
            current_symptoms += 'fever '
        if ('dib') in request.POST:
            current_symptoms += 'dib '
        if ('los') in request.POST:
            current_symptoms += 'los '
        if current_symptoms=='':
            current_symptoms = 'no'
        if ('diabetes') in request.POST:
            previous_diseases += 'diabetes '
        if ('hypertension') in request.POST:
            previous_diseases += 'hypertension '
        if ('lung') in request.POST:
            previous_diseases += 'lung '
        if ('heart') in request.POST:
            previous_diseases += 'heart '
        if ('kidney') in request.POST:
            previous_diseases += 'kidney '
        if previous_diseases=='':
            previous_diseases = 'no'
        if ('yes') in request.POST:
            travel = True
        else:
            travel = False
        if ('a') in request.POST:
            social_distance = 'Was close to someone who has tested covid positive recently.'
        elif ('b') in request.POST:
            social_distance = 'Was doing some volunteer work.'
        else:
            social_distance = 'safe'
        ques = Question.objects.create(user=request.user,temperature=temperature,current_symptoms=current_symptoms,previous_diseases=previous_diseases,travel=travel,social_distance=social_distance,timestamp=timezone.now)
        ques.save()
        return redirect('/')
    else:
        return render(request,'enter.html',{'enter':True})

def previous(request):
    d = Question.objects.filter(user=request.user)
    d = d[::-1]
    p = Person.objects.get(username=request.user.username)
    return render(request,'prev.html',{'data':d,'p':p,'prev':True})


def query(request):
    if request.method=='POST':
        if request.POST['ID'] == '':
            return render(request,'home.html')    
        name = request.POST['ID']
        if User.objects.filter(username=name).exists():
            user = User.objects.get(username=name)
            p = Person.objects.get(username=name)
            que = Question.objects.filter(user=user)
            que=que.reverse()
            if len(que)>=5:
                que=que[0:5]
            risk='low'
            s = 0
            t = 0 
            cs = 0
            for q in que:
                if q.temperature>36 and t==0:
                    t=1
                if not q.social_distance=='no' and s==0:
                    s=1
                if not q.current_symptoms=='no' and cs==0:
                    cs=1
            f = t+s+cs
            if f==1:
                risk='low'
            elif f==2:
                risk = 'moderate'
            else:
                risk = 'high'
            if len(que)==0:
                risk='low'
            return render(request,'risk.html',{'d':p,'q':que,'risk':risk})
        else:
            messages.info(request,'Wrong input/User doesn’t exist')
            return render(request,'home.html')
    else:
        return render(request,'home.html')