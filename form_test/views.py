from django.http.response import HttpResponse
from .forms import TestForm
from django.shortcuts import redirect, render

# Create your views here.
def test_view(request):
    if request.method == "POST":
        print(request.POST)
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("successful")
        return HttpResponse("unsuccessful")
    else:
        form = TestForm()
        return render(request, "test.html", {"form": form})
