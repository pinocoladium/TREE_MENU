from django.shortcuts import render

from menu.models import Menu


def index(request):
    return render(request, "index.html", {"menus": Menu.objects.all()})


def draw_menu(request, path):
    el_path = path.split("/")
    return render(
        request, "index.html", {"menu_name": el_path[0], "menu_item": el_path[-1]}
    )
