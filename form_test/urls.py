from .views import (
    register_form_view,
    prior_health_plan_form_view,
    consent_date_form_view,
)
from django.urls import path

urlpatterns = [
    path("register/", register_form_view, name="register"),
    path("prior_health/", prior_health_plan_form_view, name="prior_health_plan"),
    path("consent_date/", consent_date_form_view, name="consent_date"),
]
