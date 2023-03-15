from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, FormView
from .forms import UserAdminChangeForm, UserAdminCreationForm, UserSignupForm, UserSocialSignupForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponse

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["username", "name", 'email']
    # success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False
    # success_message = None

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


def SendEmailView(request):
    if request.method == 'POST':
        email_address = request.POST.get('email_news')
        if (email_address):
            new_user = User(username=email_address, email=email_address)
            new_user.save()
        return redirect('home')
    else:
        return render(request, 'pages/home.html')

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Override the form_valid method to redirect to home after login."""
        response = super().form_valid(form)
        return response
    
class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Override the form_valid method to redirect to home after login."""
        response = super().form_valid(form)
        return response
    
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # send the email
        send_mail(
            subject,
            f'From: {name} ({email})\n\n{message}',
            email, # from email address (optional)
            ['nguyenlenganha93nk@gmail.com'], # list of recipient email addresses
            fail_silently=False,
        )
        # return a success response
        # return HttpResponse('Success! Your message has been sent.')
        return redirect('home')
    # return an error response if the request method is not POST
    return HttpResponse('Error: Invalid request method.')