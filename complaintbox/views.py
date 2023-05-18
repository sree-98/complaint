from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# create your views here

def first(request):
    return render(request, 'index.html')

def index(request):
    return render (request, 'index.html') 

def userregister(request):
    if request.method == "POST":
        userphoto = request.FILES['userphoto']
        useremail = request.POST.get('useremail')
        username = request.POST.get('username')
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        fs = FileSystemStorage()
        filename = fs.save(userphoto.name, userphoto)
        reg = userregisters(userphoto=userphoto,useremail=useremail,username=username,userphone=userphone,password=password)
        reg.save()
        return redirect(log)
    return render(request, 'register.html', {'success':'User Registered Successfully'})


def complaint(request):
    if request.method == "POST":
        complaintto = request.POST.get('complaintto')
        date = request.POST.get('date')
        name = request.POST.get('name')
        email = request.POST.get('email')
        complaintmsg = request.POST.get('complaintmsg')
        status = request.POST.get('status')
        com = complaints(complaintto=complaintto,date=date,name=name,email=email,complaintmsg=complaintmsg,status=status)
        com.save()
        return redirect(index)
    return render(request, 'compregister.html', {'success':'Complaint Registered Successfully'})


def facregister(request):
    if request.method == "POST":
        designation = request.POST.get('designation')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fac = facregisters(designation=designation,name=name,email=email,password=password)
        fac.save()
        return redirect(facregister)
    return render (request, 'facregisterr.html', {'success':'Faculty Registered Successfully'})


def acknowledgement(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        date = request.POST.get('date')
        email = request.POST.get('email')
        ackmsg = request.POST.get('ackmsg')
        status1 = request.POST.get('status1')
        ack = acknowledgements(student_id=student_id,name=name,date=date,email=email,ackmsg=ackmsg)
        ack.save()
        return redirect(index)
    return render (request, 'acknowledgementt.html', {'success':'Acknowledgement Registered Successfully'})


def facacknowledgement(request):
    if request.method == "POST":
        date = request.POST.get('date')
        designation = request.POST.get('designation')
        name = request.POST.get('name') 
        email = request.POST.get('email')
        ackmsg = request.POST.get('ackmsg')
        faca = facacknowledgements(date=date,designation=designation,name=name,email=email,ackmsg=ackmsg)
        faca.save()
        return redirect(facacknowledgement)
    return render (request, 'facacknowledgementt.html', {'success':'Acknowledgement Registered Successfully'})


def update(request, id):
    abc = userregisters.objects.get(id=id)
    return render (request, 'updateuser.html', {'result': abc})


def update1(request, id):
        if request.method == "POST":
            userphoto = request.FILES['userphoto']
            useremail = request.POST.get('useremail')
            username = request.POST.get('username')
            userphone = request.POST.get('userphone')
            password = request.POST.get('password')
            fs = FileSystemStorage()
            filename = fs.save(userphoto.name, userphoto)
            reg = userregisters(id=id,userphoto=userphoto,useremail=useremail,username=username,userphone=userphone,password=password)
            reg.save()
            return redirect(viewuserregister)
    

def updates(request, id):
    bcd = facregisters.objects.get(id=id)
    return render(request, 'updatefac.html', {'result2': bcd})

def updates1(request, id):
    if request.method == "POST":
        designation = request.POST.get('designation')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fac = facregisters(id=id,designation=designation,name=name,email=email,password=password)
        fac.save()
        return redirect(viewfacregister)
    


def delete(request, id):
    aaa = userregisters.objects.get(id=id)
    aaa.delete()
    return redirect(viewuserregister)

def deletee(request, id):
    bbb = facregisters.objects.get(id=id)
    bbb.delete()
    return redirect(viewfacregister)

def viewuserregister(request):
    ab = userregisters.objects.all()
    return render (request, 'viewuserregisterr.html', {'result': ab} )

def viewcomplaint(request):
    ac = complaints.objects.all()
    if request.method == "POST":
        facstatus = request.POST.get('facstatus')
        com1 = admincomplaints(facstatus=facstatus)
        com1.save()
        ac1 = admincomplaints.objects.all()
    return render (request, 'viewcomplaintt.html', {'result1': ac,'result2': ac1})

def viewcomplaintadmin(request):
    ac = complaints.objects.all()
    return render (request, 'viewcomplaintsadmin.html', {'result': ac})

def viewcomplaintHr(request):
    ac = complaints.objects.filter(complaintto='HR')
    return render (request, 'viewcomplaintt.html', {'result1': ac})

def viewcomplaintTrainer(request):
    ac = complaints.objects.filter(complaintto='Trainer')
    return render (request, 'viewcomplaintt.html', {'result1': ac})

def viewcomplaintOperationshead(request):
    ac = complaints.objects.filter(complaintto='Operations Head')
    return render (request, 'viewcomplaintt.html', {'result1': ac})

def viewfacregister(request):
    ad = facregisters.objects.all()
    return render (request, 'viewfacregisterr.html', {'result2':ad})

def viewacknowledgement(request):
    s = request.session['uid']
    ae = acknowledgements.objects.filter(student_id=s)
    return render (request, 'viewacknowledgementt.html', {'result3':ae})

def viewfacacknowledgement(request):
    af = facacknowledgements.objects.all()
    return render (request, 'viewfacacknowledgementt.html', {'result4':af})

def viewfacacknowledgementTrainer(request):
    af = facacknowledgements.objects.filter(designation='Trainer')
    return render (request, 'viewfacacknowledgementt.html', {'result4':af})

def viewfacacknowledgementHr(request):
    af = facacknowledgements.objects.filter(designation='HR')
    return render (request, 'viewfacacknowledgementt.html', {'result4':af})

def viewfacacknowledgementOperationshead(request):
    af = facacknowledgements.objects.filter(designation='Operations Head')
    return render (request, 'viewfacacknowledgementt.html', {'result4':af})



def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def studentprofile(request):
    s = request.session['uid']
    vpro = userregisters.objects.get(id=s)
    return render(request, 'studentprofilee.html', {"res": vpro})


def userupdate(request, id):
    abcd = userregisters.objects.get(id=id)
    return render (request, 'updateuseradmin.html', {'result1': abcd})


def edituserprofile(request, id):
    if request.method == "POST":
        userphoto = request.FILES['userphoto']
        useremail = request.POST.get('useremail')
        username = request.POST.get('username')
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        fs = FileSystemStorage()
        filename = fs.save(userphoto.name, userphoto)
        reg = userregisters(id=id,userphoto=userphoto,useremail=useremail,username=username,userphone=userphone,password=password)
        reg.save()
        return redirect(studentprofile)
    

def adminprofile(request):
    user = request.user
    return render(request, 'adminprofilee.html', {'adn': user})


def facultyprofile(request):
    s = request.session['fid']
    fpro = facregisters.objects.get(id=s)
    return render(request, 'facultyprofilee.html', {"fac": fpro})


def adminlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password == 'admin':
        request.session['email'] = email
        request.session['admin'] = 'admin'
        return render (request, 'index.html')
    else:
        return render(request, 'logadmin.html')
    
def studentlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if userregisters.objects.filter(useremail=email,password=password).exists():
        userdetails = userregisters.objects.get(useremail=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id
            request.session['username'] = userdetails.username
            request.session['email'] = email
            request.session['user'] = 'user'
            return render(request, 'index.html')
    else:
        return render(request, 'logstudent.html')
        
def facultylogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    designation = request.POST.get('designation')
    if facregisters.objects.filter(email=email,password=password,designation=designation).exists():
        facdetails = facregisters.objects.get(email=request.POST['email'],password=password,designation=designation)
        if facdetails.password == request.POST['password']:
            request.session['fid'] = facdetails.id
            request.session['username'] = facdetails.name
            request.session['email'] = email
            request.session['user'] = 'user'
            request.session['designation'] = designation
            return render(request, 'index.html')
    else:
        return render(request, 'logfaculty.html')
    
def log(request):
    return render (request, 'log.html')


