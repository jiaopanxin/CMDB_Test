from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
from django.views.generic.edit import FormView
from users.users_forms import UserRegisterModelForm
from users.models import UsersProfile
from django.urls import reverse,reverse_lazy

class UserRegisterFormView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterModelForm
    success_url = reverse_lazy('users:login')
    def form_valid(self, form):
        user = UsersProfile(**form.cleaned_data)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        print("form-->", form)
        return super().form_invalid(form)




class UserLoginView(LoginView):
        template_name='users/login.html'


class UserLogoutView(LogoutView):
        next_page=reverse_lazy('index')


from django.contrib.auth.hashers import make_password,check_password

def UserPasswordRewriteView(request):    
    name = request.POST.get('username')
    pwd = request.POST.get('old_password')   
    user = UsersProfile.objects.get(username=name)
    if name == user.username and check_password(pwd,user.password):
        pwd_md5 = make_password(request.POST.get("password"))
        user.password = pwd_md5
        user.save()
        return render(request, 'users/login.html')
    else:
        return HttpResponse("你没有操作权限")