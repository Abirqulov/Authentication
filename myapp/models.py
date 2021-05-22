from django.db import models


class UserAccount(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Order(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Restourant(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='myapp/images/')
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FastFoodMenu(models.Model):
    restaran = models.ForeignKey(Restourant, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=80)
    image = models.ImageField(upload_to='myapp/images/')

    def __str__(self):
        return self.title
