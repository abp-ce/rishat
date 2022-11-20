from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('buy/<id>/', views.buy_item, name='buy_item'),
    path('buy_order/<id>/', views.buy_order, name='buy_order'),
    path('item/<id>/', views.get_item, name='get_item'),
    path('order/<id>/', views.get_order, name='get_order'),
]
