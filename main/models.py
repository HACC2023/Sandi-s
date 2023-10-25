from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)


class ReusableItem(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
