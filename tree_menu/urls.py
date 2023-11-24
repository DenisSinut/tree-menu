from django.urls import path
from tree_menu.views import MenuView, menu

app_name = 'tree_menu'

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    path('<str:menu_url>/', menu, name='menu'),
]