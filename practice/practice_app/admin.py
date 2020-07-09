from django.contrib import admin
from .models import *

admin.site.register(Person, PersonAdmin)
admin.site.register(PersonDetails, PersonDetailsAdmin)
admin.site.empty_value_display = 'InvalidName'
# admin.site.register(PersonAdmin)
# admin.site.register(Author)
# admin.site.register(Publisher)
# admin.site.register(Store)
# admin.site.register(Book)