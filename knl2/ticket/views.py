from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
# from .models import ToDoList, Item
# from .forms import CreateNewList

# Create your views here.
def plan_base(response):
        return render(response, "templates/services/plan_base.html", {})

# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_view(response):
    if response.method == 'POST':
        return render(response, "templates/services/payment.html", {})
    #     # Use the Stripe library to create a payment token from the credit card info
    #     token = stripe.Token.create(
    #         card={
    #             "number": request.POST['card_number'],
    #             "exp_month": request.POST['exp_month'],
    #             "exp_year": request.POST['exp_year'],
    #             "cvc": request.POST['cvc']
    #         }
    #     )

    #     # Use the payment token to charge the user's credit card and complete the payment
    #     charge = stripe.Charge.create(
    #         amount=1000,  # amount in cents
    #         currency='euro',
    #         description='Exemple payment',
    #         source=token
    #     )

    #     # Display a success message to the user
    #     return render(request, 'templaces/services/payment_success.html')
    # else:
    #     # Display the payment form to the user
    #     return render(request, 'templaces/services/payment_form.html')

