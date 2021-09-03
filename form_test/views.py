from django.http.response import HttpResponse

# from .forms import TestForm
from django.shortcuts import redirect, render
from .forms import ConsentDateForm, PriorHealthPlanForm, RegisterForm
from .models import ConsentDateModel, PriorHealthPlanModel, RegisterModel
import json

# Create your views here.


def index(request):
    if request.method == "POST":
        return redirect(register_form_view)
    return render(request, "index.html")


def data_fetch_strategy(request):
    return render(request, "data_fetch_strategy.html")


def register_form_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(data_fetch_strategy)
        return HttpResponse("unsuccessful")
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})


def prior_health_plan_form_view(request):

    if request.method == "POST":
        form = PriorHealthPlanForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(consent_date_form_view)
        return HttpResponse("unsuccessful")
    else:
        form = PriorHealthPlanForm()
        return render(request, "prior_health_plan.html", {"form": form})


def consent_date_form_view(request):

    if request.method == "POST":
        form = ConsentDateForm(request.POST)
        if form.is_valid():
            form.save()
            consent_date_data = vars(ConsentDateModel.objects.all().last())
            register_data = vars(RegisterModel.objects.all().last())
            prior_health_data = vars(PriorHealthPlanModel.objects.all().last())
            final_data = {**register_data, **prior_health_data, **consent_date_data}
            final_data.pop("_state")
            final_data["date"] = final_data["date"].strftime("%d-%m-%Y")
            final_data["date_of_birth"] = final_data["date_of_birth"].strftime(
                "%d-%m-%Y"
            )
            final_data_json = json.dumps(final_data)
            return HttpResponse(final_data_json)
        return HttpResponse("unsuccessful")
    else:
        form = ConsentDateForm()
        return render(request, "consent_date.html", {"form": form})
