from django.db import models



class userregisters(models.Model):
    userphoto = models.CharField(max_length=150)
    useremail = models.EmailField(max_length=150)
    username = models.CharField(max_length=150)
    userphone = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

class complaints(models.Model):
    complaintto = models.CharField(max_length=150)
    date = models.DateField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    complaintmsg = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

class facregisters(models.Model):
    designation = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)

class acknowledgements(models.Model):
    student_id =models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    date = models.DateField(max_length=150)
    email = models.EmailField(max_length=150)
    ackmsg = models.CharField(max_length=150)

class facacknowledgements(models.Model):
    date = models.DateField(max_length=150)
    designation = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    ackmsg = models.CharField(max_length=150)

class admincomplaints(models.Model):
    facstatus = models.CharField(max_length=150)