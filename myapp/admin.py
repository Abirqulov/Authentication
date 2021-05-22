from django.contrib import admin
from .models import UserAccount, Restourant, FastFoodMenu, Category

admin.site.register(UserAccount)
admin.site.register(Restourant)
admin.site.register(FastFoodMenu)
admin.site.register(Category)

