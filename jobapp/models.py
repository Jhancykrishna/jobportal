from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    Phone = models.CharField(max_length=13)
    options = (("male", "male"),
               ("female", "female"),
               ("others", "others"))
    gender = models.CharField(max_length=15,choices=options,default="male")
    options = (("employer", "employer"),
               ("jobseeker", "jobseeker"))
    user_type = models.CharField(max_length=12,choices=options,default="employer")

class JobseekerModel (models.Model):

    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=20)
    University = models.CharField(max_length=20)
    skills = models.CharField(max_length=200)
    experience = models.FloatField()
    expected_salary = models.IntegerField()
    ready_to_relocate = models.BooleanField(default=True)

class EmployerModel(models.Model):

    company_name = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    company_address = models.CharField(max_length=120)

class JobModel(models.Model):
    job_role = models.CharField(max_length=20)
    employer = models.ForeignKey(EmployerModel, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, default="")
    job_details = models.CharField(max_length=120)
    exp_required = models.CharField(max_length=15)
    openings = models.IntegerField()
    options = (("Active", "Active"),
               ("Closed", "Closed"))
    status = models.CharField(max_length=10, choices=options, default="Active")
    starting_date = models.DateField(auto_now=True)
    last_date = models.DateField()

class JsJobModel(models.Model):
    job_role = models.CharField(max_length=20)
    employer = models.ForeignKey(EmployerModel, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, default="")
    job_details = models.CharField(max_length=120)
    exp_required = models.CharField(max_length=15)
    openings = models.IntegerField()
    options = (("Active", "Active"),
               ("Closed", "Closed"))
    status = models.CharField(max_length=10, choices=options, default="Active")
    starting_date = models.DateField(auto_now=True)
    last_date = models.DateField()

class Applications(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE,default="")
    job_seeker = models.CharField(max_length=20,default="")
    options = (("received", "received"),
               ("viewed", "viewed"),
               ("selected", "selected"),
               ("rejected", "rejected"))
    status = models.CharField(max_length=20,choices=options, default="Received")







