from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<id>/', views.buy_item, name='buy_item'),
    path('item/<id>/', views.get_item, name='get_item'),
    path('order/<id>/', views.get_order, name='get_order'),
]
