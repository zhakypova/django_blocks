from django.contrib import admin

from .models import Block, Apartment
from .forms import BlockForm,ApartmentForm

# @admin.display(description='Итоговая стоимость всех квартир в блоке')
# def total_cost_apart(obj):
#     cost_apart = obj.get_all_apartments * obj.get_total_cost
#     return cost_apart

class AdminMixin:
    empty_value_display = '--без хоз--'
    actions_on_bottom = True
    actions_on_top = False

@admin.register(Apartment)
class ApartmentAdmin(AdminMixin, admin.ModelAdmin):
    date_hierarchy = 'date_of_sale'
    list_filter = ('bloc', 'status',)
    search_fields = ('name',)
    fields = ('name', 'date_of_sale', 'status', 'total_area', )
    form = ApartmentForm
    list_display = ('name', 'date_of_sale', 'status', 'total_area', 'get_total_cost',)

@admin.register(Block)
class BlockAdmin(AdminMixin, admin.ModelAdmin):
    search_fields = ('status',)
    list_display = ('number', 'porch', 'floors', 'apartments_on_floor', 'get_all_apartments', )



