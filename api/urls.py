from django.urls import path,include
from .  import views
from django.views.generic import TemplateView

app_name="api"

urlpatterns = [
    path('asset-info/',views.ApiView.as_view(),name="ApiView"),

]