from django.shortcuts import render
from django.http import HttpResponse
from FoodApp.models import Item

# Create your views here.
def index(request):
      item_list=Item.objects.all()
      context={
            'item_list':item_list,
      }
      return render(request, 'FoodApp/index.html',context)

def detail(request,item_id):
      item=Item.objects.get(pk=item_id)
      context={
            'item': item,
      }
      return render(request, 'FoodApp/detail.html',context)
