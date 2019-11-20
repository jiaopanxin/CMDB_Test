from django.urls import path
from django.views.generic import TemplateView


from . import views

app_name = "users"
urlpatterns = [
    path('register/', views.UserRegisterFormView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('rewrite/', TemplateView.as_view(template_name="users/rewrite.html"), name="rewrites"),
    path('rewrites/', views.UserPasswordRewriteView, name="rewrite"),
    path('lock_screen/', TemplateView.as_view(template_name="base.html"),
         name="lock_screen"),
]
