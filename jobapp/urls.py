from django.urls import path
from.views import Index,Homepage,Logout,PortalRegistrationView,LoginView, JobsView,\
          EmployerRegView, JobsCreateView, JobseekerRegView, JobsListView, JobsDetailView, JobsDeleteView, \
          JobsUpdateView,JobseekerListView, JobApplyView, ApplicationlistView, ApplicationDetailView, \
          ApplicantDetailView



urlpatterns = [
    path("", Index, name="index"),
    path("home", Homepage, name="home"),
    path("register", PortalRegistrationView.as_view(), name="register"),
    path("employer", EmployerRegView.as_view(), name="empregistration"),
    path("post", JobsCreateView.as_view(), name="jobpost"),
    path("jobslist", JobsListView.as_view(), name="jobslist"),
    path("jobsdetail/<int:pk>", JobsDetailView.as_view(), name="detail"),
    path("jobsupdate/<int:pk>", JobsUpdateView.as_view(), name="update"),
    path("jobsdelete/<int:pk>", JobsDeleteView.as_view(),name="delete"),
    path("applications",ApplicationlistView.as_view(),name="viewapp"),
    path("applicant/<int:pk>",ApplicantDetailView.as_view(),name="info"),
    path("appdetail/<int:pk>",ApplicationDetailView.as_view(),name="appdetail"),
    path("jobseeker", JobseekerRegView.as_view(), name="jobseeker"),
    path("view", JobseekerListView.as_view(), name="employeelist"),
    path("apply/<int:pk>", JobApplyView, name="apply"),
    path("jobview", JobsView.as_view(), name="jslist"),
    path("login", LoginView.as_view(), name="signin"),
    path("logout", Logout.as_view(), name="signout"),


]