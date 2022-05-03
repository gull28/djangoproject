from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .models import User
from .forms import CreateNewList
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = 1
                    else:
                        item.complete = 0

                    item.save()
            elif response.POST.get("additem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=0)
                else:
                    print("invalid")

        return render(response, "ecomshop/listing.html", {"ls": ls})
    return render(response, "ecomshop/home.html", {"ls": ls})


def home(response):
    return render(response, "ecomshop/home.html")


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "ecomshop/create.html", {"form": form})


def view(response):
    return render(response, "ecomshop/view.html", {})


@login_required
def account(response):
    return render(response, "ecomshop/account.html", {})
