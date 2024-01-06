from django.contrib import admin

from .models import Cat, Pair

# Register your models here.


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass


@admin.register(Pair)
class PairAdmin(admin.ModelAdmin):
    pass
