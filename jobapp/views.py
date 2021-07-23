from django.shortcuts import render,redirect, get_object_or_404
from .models import MyUser,EmployerModel,JobseekerModel,JobModel,Applications
from .forms import RegistrationForm,LoginForm,EmployerForm,JobseekerForm,JobForm,ApplicationForm
from django.views.generic import CreateView,ListView,TemplateView,DetailView,DeleteView,UpdateView
from django.contrib.auth import logout,authenticate,login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .decorators import loginrequired


# Create your views here.

def Index(request):
    return render(request,"index.html")

def Homepage(request):
    return render(request,"home.html")



class Logout(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")


class PortalRegistrationView(CreateView):
    model=MyUser
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("signin")

class JobsView(ListView):
    model = JobModel
    template_name = "jobs.html"
    context_object_name = "jobs"

class LoginView (TemplateView):
    model = MyUser
    form_class = LoginForm
    template_name = "login.html"
    context = {}

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get("Username")
            password = form.cleaned_data.get("Password")
            print(username)

            user = authenticate(request, username=username, password=password)
            if user:
                print("success")
                login(request,user)
                if (request.user.user_type == "employer"):

                    return redirect("empregistration")
                else:
                    return redirect("employeelist")


            else:
                print("failure")
        return render(request,self.template_name,self.context)




@method_decorator (loginrequired, name='dispatch')
class EmployerRegView(CreateView):
    model = EmployerModel
    form_class = EmployerForm
    template_name = "empregistration.html"
    success_url = reverse_lazy("jobpost")


class JobsCreateView(CreateView):
    model = JobModel
    form_class = JobForm
    template_name = "jobpost.html"
    success_url = reverse_lazy("jobslist")

class JobsListView(ListView):
    model = JobModel
    template_name = "jobslist.html"
    context_object_name = "jobs"

class JobsDetailView(DetailView):
    model = JobModel
    template_name = "jobdetail.html"
    context_object_name = "job"

class JobsUpdateView(UpdateView):
    model = JobModel
    form_class = JobForm
    template_name = "update.html"
    success_url = reverse_lazy("jobslist")

class JobsDeleteView(DeleteView):
    model = JobModel
    template_name = "delete.html"
    success_url = reverse_lazy("jobslist")


@method_decorator(loginrequired, name='dispatch')
class JobseekerRegView(CreateView):
    model = JobseekerModel
    form_class = JobseekerForm
    template_name = "jobseekerreg.html"
    success_url = reverse_lazy("jslist")

class JobseekerListView(ListView):
    model = JobModel
    template_name = "jobseekerlist.html"
    context_object_name = "jobs"

def JobApplyView(request,*args,**kwargs):
    jid = kwargs.get("pk")
    job = JobModel.objects.get(id=jid)

    application = Applications(job=job, job_seeker=request.user)
    application.save()
    return redirect("employeelist")

def Remove_application(request,*args,**kwargs):
    jid = kwargs.get("pk")
    job = JobModel.objects.get(id=jid)
    job.delete()
    return redirect("employeelist")


class ApplicationlistView(ListView):
    model = Applications
    template_name = "applicationform.html"
    context_object_name = "apps"

    def get_queryset(self):
        queryset = super(ApplicationlistView, self).get_queryset()
        queryset = queryset.filter(job__employer__company_name__username=self.request.user)
        return queryset

    # context = {}
    #
    # def get(self, request, *args, **kwargs):
    #     applications = self.model.objects.filter(job__employer__company_name__username=self.request.user)
    #     return render(request, self.template_name, self.context)


class ApplicationDetailView(DetailView):
    model = Applications
    template_name = "applicationdetail.html"
    context_object_name = "app"

class ApplicantDetailView(DetailView):
    model = JobseekerModel
    template_name = "applicantinfo.html"
    context_object_name = "employee"

