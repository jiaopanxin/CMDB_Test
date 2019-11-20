from django.urls import path, include
from . import views
from django.views.generic import TemplateView


app_name = "octoups"

urlpatterns = [
    path("connection/",views.ConnectionView.as_view(),name="connection"),
    path("run/",views.ExecCommandView.as_view(),name="run"),
    path("get_result/",views.CommandResultView.as_view(),name="get_result"),
    path("async/",views.AsyncDemoView.as_view(),name="async"),
    path("ansible-adhoc",views.AnsibleAdhocView.as_view(),name="anisble-hoc")
]
