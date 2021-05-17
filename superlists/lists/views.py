from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, "home.html")


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST["item_text"], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, "home.html", {"error": error})
    return redirect("view_list", list_.id)


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == "POST":
        try:
            item = Item(text=request.POST["item_text"], list=list_)
            item.full_clean()
            item.save()
            return redirect(f"/lists/{list_.id}/")
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, "list.html", {"list": list_, "error": error})