from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

#These are the views that would have allowed us to process the login/logout thing without oauth, but unfortunately I didn't really manage to develop this feature.

class LoginView(TemplateView):

  template_name = 'microblog/login.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'microblog/login.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)