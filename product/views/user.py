from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView

from product.forms import CustomAuthenticationForm
from product.utils.pwned import PwnedPasswordsValidator


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        password = form.cleaned_data['password']
        validator = PwnedPasswordsValidator()
        try:
            validator.validate(password)
        except ValidationError:
            self.request.session['password_pwned'] = True
        else:
            self.request.session['password_pwned'] = False
        return super().form_valid(form)


class UserLogoutView(TemplateView):
    title = 'Logout'
    template_name = 'registration/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs.get('title', self.title)
        return context

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(request.get_full_path())
