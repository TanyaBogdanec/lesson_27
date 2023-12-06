from django.contrib import admin
from .models import Account, Product
from .models import User


admin.site.register(Account)
admin.site.register(User)
admin.site.register(Product)
