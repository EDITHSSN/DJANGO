from this import d
from django.shortcuts import render
from club.models import *
from django.http import HttpResponse , HttpResponseRedirect
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'land.html')
    
def login(request):
    if request.method == 'POST':
        ema = request.POST['email']
        passw= request.POST['password']
        try:
            if student.objects.get(email=ema,password=passw):
                s=student.objects.get(email=ema,password=passw)
                if s.postv == 3:
                    return  HttpResponseRedirect(f'/guest/login/editor_profile/?ema={ema}',) 
                else:
                    return HttpResponseRedirect(f'/guest/login/profile/?ema={ema}',) 
        except:
            return render(request, 'test.html',{'ema':ema,'passw':passw,'student':student.objects.all()})
    else:
        return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        ema = request.POST['email']
        passw= request.POST['password']
        pos= request.POST['posting']
        print(ema,passw)
        try:
            if student.objects.get(email=ema):
                return HttpResponse('/guest/login/')
        except:
            s=student(email=ema,password=passw,postv=pos)
            s.save()
            return render(request, 'personal_form.html',{'ema':ema,'passw':passw,})
    else:
        return render(request,'login.html')


def profile(request):
    s=student.objects.get(email=request.GET['ema'])
    
    if s.postv == 3:
        context={'name':s.name,'dept':s.dept,'year':s.year,'clubsinterested':s.clubsinterested,'ema':s.email }
        return render(request,'editor_profile.html',context)
    else:
        context={'name':s.name,'dept':s.dept,'year':s.year,'clubsinterested':s.clubsinterested,'ema':s.email}
        return render(request,'profile.html',context)


def editor_profile(request):
    s=student.objects.get(email=request.GET['ema'])
    if s.postv == 3:
        e=event.objects.all()
        evid=[]
        for entry in e:
            evid.append(entry)
            print("Evname", entry.event_name)
        context={'name':s.name,'dept':s.dept,'year':s.year,'clubsinterested':s.clubsinterested,'ema':s.email,'events':evid }
        return render(request,'editor_profile.html',context)
    else:
        return render(request,'profile.html',context)


'''def club(request):
    return render(request,'club.html')'''

def details(request):
    if request.method == 'POST':
        ema = request.POST['ema']
        passw= request.POST['passw']
        if student.objects.get(email=ema,password=passw):
            s=student.objects.get(email=ema,password=passw)
            s.name=request.POST['name']
            s.dept=request.POST['dept']
            s.year=request.POST['year']
            s.clubsinterested=request.POST['clubinterested[]']
            s.student_id = s.id
            s.save()
            print(request.POST['name'], request.POST['dept'], request.POST['year'], request.POST['clubinterested[]'])
            return HttpResponseRedirect('/guest/login/profile')
    else:   
        return render(request,'personal_form.html')

def test(request):
    return render(request,'test.html',context={'student':student.objects.all(),'ema':request.GET['ema'],'passw':request.GET['passw']})

def eventt(request):
    if request.method == 'POST':
        evname = request.POST['evname']
        des_ev = request.POST['desc_ev']
        date = request.POST['date']
        vol = request.POST['volunteers']
        s = student.objects.get(email=request.GET['ema'])
        print("evname:" , s.student_id)
        c = club.objects.get(club_name = s.clubsinterested)
        e=event(event_name = evname , description_event=des_ev , date=date , volunteers=vol,club_name = c.club_name,club_id = c.club_id,student_id = s.id)
        e.save()
        return HttpResponseRedirect('/guest')
    else:
        return render(request,'event_form.html')

def pevent(request):
    s=event.objects.get(id=request.GET['id'])
    if request.method == 'POST':
        status = request.POST['status']
        s.status=status
        s.save()
        return HttpResponseRedirect('/guest/login/editor_profile')
    else:
        context={'name':s.event_name,'description_event':s.description_event,'volunteers':s.volunteers, 'date':s.date}
        return render(request,'print_form.html',context)

def forgotp(request):
    if request.method == 'POST':
        ema = request.POST['email']
        try:
            if student.objects.get(email=ema):
                return HttpResponseRedirect(f'/guest/login/change_password/?email={ema}',)
        except:
            message="Email not found"
            return render(request,'indexx.html' , {'message':message})
    else:
        return render(request,'indexx.html')

def change_password(request):
    if request.method == 'POST':
        s=student.objects.get(email=request.GET['email'])
        s.password=request.POST['password']
        s.save()
        return HttpResponseRedirect('/guest/login/')
    else:
        message="password not changed"
        return render(request,'indexx.html', {'message':message})


def club_page(request):
        print("club name:",request.GET['club_name'])
        c = club.objects.get(club_name=request.GET['club_name'])
        e=event.objects.filter(club_id=c.club_id)
        evid=[]
        for entry in e:
            evid.append(entry)
        return render(request, 'club_page.html', {'club':c,'events':evid})

def chat(request):
    if request.method == 'POST':
        if request.POST['submit']=='add':
            title=request.POST['title']
            comment=request.POST['comment']
            print("title:",title,"comment:",comment)
            s=student.objects.get(email=request.GET['email'])
            c=comments(title=title,comment=comment,student_id=s.id,date=datetime.now())
            c.save()
            c=comments.objects.all()
            t=threads.objexts.all()
            context = {'comments':c,'threads':t}
            return render(request,'chat.html',context)
        else:
            thread_description=request.POST['thread_description']
            id = request.POST['submit']
            print("thread:",thread_description,"id:",id)
            t=threads(thread=thread_description,comments_id=id,date=datetime.now())
            t.save()
            c=comments.objects.all()
            t=threads.objects.all()
            context = {'comments':c,'threads':t}
            return render(request,'chat.html',context)
    else:
        s=student.objects.get(email=request.GET['email'])
        c=comments.objects.all()
        t=threads.objects.all()
        context = {'comments':c,'threads':t}
        return render(request,'chat.html',context)