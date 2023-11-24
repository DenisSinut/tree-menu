from django import template
from tree_menu.models import Menu
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = Menu.objects.all()
    return mark_safe(render_menu(menu, menu, menu_name))



def render_menu(all_menu, menu, name):
    if name:
        for item in all_menu:
            if item.name == name:
                menu_item = item
    else:
        menu_item = menu
    menu_html = '<ul>'
    menu_html += '<li>'
    if menu_item.url:
        menu_html += f'<a href="{menu_item.url}">{menu_item.name}</a>'
    elif menu_item.named_url:
        menu_html += f'<a href="{menu_item.named_url}">{menu_item.name}</a>'
    else:
        menu_html += menu_item.name
    for item in all_menu:
        if item.parent_id == menu_item.id:
            menu_html += render_menu(all_menu, item, None)
    menu_html += '</li>'
    menu_html += '</ul>'

    return menu_html
