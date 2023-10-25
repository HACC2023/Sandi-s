from django.shortcuts import render

from .models import Owner, ReusableItem


def index(request):
    owner_list = Owner.objects.order_by("name")[:5]
    context = {"owner_list": owner_list}
    return render(request, "main/owner_list.html", context)
