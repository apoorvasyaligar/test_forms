from django.http.response import HttpResponse

# from .forms import TestForm
from django.shortcuts import redirect, render
from .forms import ConsentDateForm, PriorHealthPlanForm, RegisterForm

# Create your views here.


def index(request):
    if request.method == "POST":
        return redirect(register_form_view)
    return render(request, "index.html")


def data_fetch_strategy(request):
    return render(request, "data_fetch_strategy.html")


def register_form_view(request):

    if request.method == "POST":
        print(request.POST)
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
        print(request.POST)
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
        print(request.POST)
        form = ConsentDateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("successful")
        return HttpResponse("unsuccessful")
    else:
        form = ConsentDateForm()
        return render(request, "consent_date.html", {"form": form})
