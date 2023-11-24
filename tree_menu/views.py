from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from tree_menu.models import Menu


class MenuView(TemplateView):
    template_name = 'tree_menu/menu.html'


def menu(request, menu_url):
    return render(request, 'tree_menu/menu.html')



