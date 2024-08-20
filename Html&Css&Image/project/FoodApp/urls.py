from django.urls import path
from . import views

app_name='FoodApp'
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:item_id>/',views.detail,name='detail'),
]