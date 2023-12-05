from django import template
from django.core.exceptions import ObjectDoesNotExist

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu.html")
def draw_menu(menu_name: str = None, menu_item: str = None):
    def get_menu(menu_item: str = None, submenu: list = None):
        if menu_item is None:
            menu = list(items.filter(parent=None))
        else:
            menu = list(items.filter(parent__name=menu_item))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(items.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return get_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    items = MenuItem.objects.filter(menu__name=menu_name)
    if menu_name == menu_item:
        return {"menu": get_menu()}
    else:
        return {"menu": get_menu(menu_item)}
