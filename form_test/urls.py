from .views import (
    data_fetch_strategy,
    register_form_view,
    prior_health_plan_form_view,
    consent_date_form_view,
    index,
)
from django.urls import path

urlpatterns = [
    path("", index),
    path("data_fetch/", data_fetch_strategy),
    path("register/", register_form_view, name="register"),
    path("prior_health/", prior_health_plan_form_view, name="prior_health_plan"),
    path("consent_date/", consent_date_form_view, name="consent_date"),
]
