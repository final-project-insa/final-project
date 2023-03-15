from django.urls import path
from ticket import views

urlpatterns = [
    # path("create/", views.create, name="create"),
    # path("view/", views.view, name="view"),
    path("plan_base/", views.plan_base, name="plan_base"),
]