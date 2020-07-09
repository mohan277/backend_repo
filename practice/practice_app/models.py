from django.contrib import admin
from django.db import models
from django.utils.html import format_html




class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)



class PersonAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')


class PersonDetails(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(auto_now=True)
    color_code = models.CharField(max_length=6)

    def colored_name(self):
        return format_html(
            '<span style="color: {};">{}</span>',
            self.color_code,
            self.name
        )
    colored_name.admin_order_field = 'name'

    def decade_born_in(self):
        return self.birthday.strftime('%Y')[:3] + "0's"
    decade_born_in.short_description = 'Birth decade'


    def born_in_fifties(self):
        return self.birthday.strftime('%Y')[:3] == '195'
    born_in_fifties.boolean = True

class PersonDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'decade_born_in', 'colored_name', 'born_in_fifties')



# from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

# class Publisher(models.Model):
#     name = models.CharField(max_length=300)

# class Book(models.Model):
#     name = models.CharField(max_length=300)
#     pages = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     rating = models.FloatField()
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     pubdate = models.DateField()

# class Store(models.Model):
#     name = models.CharField(max_length=300)
#     books = models.ManyToManyField(Book)



