from django.contrib import admin
from vendor.models import Category,Author,Books
# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Books)