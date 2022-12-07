from django.db import models
from django.urls import reverse_lazy
from django.contrib import admin

class Block(models.Model):
    number = models.IntegerField(verbose_name='Номер блока')
    price = models.IntegerField(verbose_name='Стоимость за квадратный метр квартиры')
    porch = models.IntegerField(verbose_name='Количество подъездов')
    floors = models.IntegerField(verbose_name='Количество этажей')
    apartments_on_floor = models.IntegerField(verbose_name='Количество квартир на этаж')

    def __str__(self):
        return f'{self.number} - {self.price}'

    def get_absolut_url(self):
        return reverse_lazy('', kwargs = {'id': self.id})


    @admin.display(description='Общее количество квартир')
    def get_all_apartments(self):
        return self.apartments_on_floor * self.floors



class Apartment(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО владельца', null=True, blank=True)
    date_of_sale = models.DateField(verbose_name='Дата продажи', null=True, blank=True)
    status = models.CharField(max_length=20, verbose_name='Статус', choices=(
        ('Выкуп','выкупили'),('Выкуп не до конца','не до конца'),
        ('Расторгнуто','расторг'),('Не продано','не прод'))
                               )
    bloc = models.ForeignKey(Block, on_delete=models.CASCADE)
    total_area = models.IntegerField(verbose_name='общая площадь (кв.м)')

    def __str__(self):
        return f'{self.name} - {self.status}'

    def get_absolut_url(self):
        return reverse_lazy('', kwargs={'pk': self.id})

    @admin.display(description='Общая стоимость')
    def get_total_cost(self):
        total_cost = self.total_area * self.bloc.price
        return total_cost

