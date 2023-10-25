from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Owner, ReusableItem

import json


def index(request):
    owner_list = Owner.objects.all()
    context = {"owner_list": owner_list}
    return render(request, "main/owner_list.html", context)


def register_owner(request):
    name = request.GET["name"]
    o = Owner.objects.filter(name=name)
    if (len(o) > 0):
        return JsonResponse({'Error': "Business already exists"})
    o = Owner(name=name)
    o.save()
    return JsonResponse({'owner': str(o)})


def register_reusable_item(request):
    id = request.GET["id"]
    price = request.GET["price"]
    owner = Owner.objects.filter(id=id)
    if (len(owner) == 0):
        return JsonResponse({'Error': "Owner doesn't exist"})
    owner = owner[0]
    ri = ReusableItem(owner=owner, price=price)
    ri.save()
    return JsonResponse({'reusable_item': str(ri)})


def owner_reusable_items(request):
    id = request.GET["id"]
    owner = Owner.objects.filter(id=id)[0]
    li = list(ReusableItem.objects.filter(owner=owner))
    result = []
    for i in li:
        result.append(str(i))
    print(len(result))
    return JsonResponse({'reusable_items': result})


def reusable_items(request):
    ri = ReusableItem.objects.all()
    context = {"ri_list": ri}
    result = []
    for i in list(ri):
        result.append(str(i))
    return JsonResponse({'reusable_items': result})
