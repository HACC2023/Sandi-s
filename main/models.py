from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str({"id": self.id, "name": self.name})


class ReusableItem(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default='0.00')

    def __str__(self):
        return str({"owner": self.owner,
                    "link": self.link,
                    "in_stock": self.in_stock,
                    "price": self.price})
