from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job
from .models import Contact as cd
from .models import Applicant
from .models import Hiring
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import math
from django.contrib.auth.models import User
from .forms import MyUserForm
# Create your views here.

def user_login(request):
     if request.method == 'POST':
        loguname = request.POST['username']
        logpassword=request.POST['password']

        user = authenticate(username=loguname, password=logpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'sucessfully logged in')
            return redirect('home')
        else :
            messages.error(request, "Invalid Credentials")
            return redirect('home')
def user_logout(request):
    logout(request)
    messages.success(request, 'sucessfully loged out!')
    return redirect('home')

def contact(request):
    if(request.method == 'POST'):
        #on server side we take the name of form into consideration as data sent from form is in key: values where
        #key= name , value=value
        c_name=request.POST['name']
        c_email=request.POST['email']
        c_subject=request.POST['subject']
        c_message=request.POST['message']
        
        cdata=cd(name=c_name, email=c_email, subject=c_subject, message= c_message )
        print(cdata)
        cdata.save()
        messages.success(request, 'sucessfully Contact Subitted')
        return redirect('home')
    else:
        return render(request, '../templates/contact.html')

def hire(request):
    if request.method == 'POST':
        job=request.POST['job']
        cat=request.POST['cat']
        expe=request.POST['expe']
        desc=request.POST['desc']
        pub_date=request.POST['pub_date']
        location=request.POST['location']
        new_job=jb(job= job, cat= cat, desc= desc , pub_date=pub_date ,expe=expe ,location=location)
        new_job.save()
        messages.success(request, 'Job uploaded Sucessfully')
        return redirect('home')
    else:
        return render(request,'job_upload.html')
    

def handlesignin(request):
    if request.method == "POST":
        form = MyUserForm(request.POST, request.FILES)
        form.save()
        message.success(request,'Sucessfully created.')
            # Handle invalid login here. You can display an error message or redirect to another page.
        return redirect('home')  # For example, redirect to the login page again.
    else:
        form = MyUserForm()
        return render(request, '../templates/candidate_register.html', {'form': form})

def search(request):
  if request.method == 'POST':
    sub_cat=request.POST['cat']
    if(sub_cat=='all'):
        filtered=list(Job.objects.all())
    else:
        filtered = list(Job.objects.filter(cat = sub_cat))
    flag=1
    return render(request, '../templates/home.html',{'categorywise' : filtered, 'flag': flag})
  else:
        # If it's a GET request, you can either return an empty search page or redirect to the home page
        # For example, redirecting to the home page:
        return redirect('home')
def home(request):
    return render(request, '../templates/home.html')

from django.shortcuts import render, get_object_or_404

def apply_job(request):
    if request.method == 'POST':
        _id=request.POST['id']
        job=Job.objects.get(id=_id)
        user_id=request.user.id
        # Assuming you have a logged-in user, you can get the user's ID
        try:
            applicant = Applicant.objects.get(candidate=user_id)
            if _id not in applicant.job_list:
                applicant.job_list.append(_id)
                applicant.save()
                messages.success(request, 'sucessfully Applied!')
        except Applicant.DoesNotExist:
            # If applicant doesn't exist, create a new one
            applicant = Applicant.objects.create(candidate=user_id, job_list=[job_id])

    # You can redirect the user to a success page or the same page after applying
    return redirect('home')


def tracker(request):
     if request.method == 'GET':
        track_result = None
        select_track = request.GET.get('select_track')
        app_id = request.GET.get('id')
        send_list=[]
        if select_track and app_id:
            if select_track == 'job':
                try:
                    jb = Hiring.objects.get(job_id=app_id)
                    track_result = f"Job ID: {jb.job_id}, Applied Candidates IDs: {jb.candidate_list}"
                    for item in jb.candidate_list:
                        send_list.append(User.objects.get(pk=item))
                except Hiring.DoesNotExist:
                    track_result = "Job not found."
            elif select_track == 'applicant':
                try:
                    applicant = Applicant.objects.get(candidate=app_id)
                    track_result = f"Applicant ID: {applicant.candidate}, Applied In Jobs: {applicant.job_list}"
                    for item in applicant.job_list:
                        send_list.append(Job.objects.get(pk=item))
                except Applicant.DoesNotExist:
                    track_result = "Applicant not found."

     return render(request, '../templates/track.html', {'track_result': track_result, 'send_list': send_list})
