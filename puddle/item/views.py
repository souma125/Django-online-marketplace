from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Item
# Create your views here.
def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
        'item':item,
        'related_items':related_items
    })
def edit(request,pk):
    pass
def delete(request,pk):
    pass    