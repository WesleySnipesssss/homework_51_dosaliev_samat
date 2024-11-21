from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import CatNameForm, InteractionForm
from .models import Cat

cat_instance = None

def welcome(request):
    global cat_instance
    if request.method == "POST":
        form = CatNameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            cat_instance = Cat.objects.create(name=name)
            return redirect("cat_info")
    else:
        form = CatNameForm()
    return render(request, "cat_app/welcome.html", {"form": form})

def cat_info(request):
    global cat_instance
    if not cat_instance:
        return redirect("welcome")

    if request.method == "POST":
        form = InteractionForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data["action"]
            if action == "feed":
                cat_instance.feed()
            elif action == "play":
                cat_instance.play()
            elif action == "sleep":
                cat_instance.sleep()
    else:
        form = InteractionForm()

    return render(request, "cat_app/cat_info.html", {"cat": cat_instance, "form": form})
