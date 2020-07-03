from django.db import models

# Create your models here.

"""categary model for storing category names"""
class Category(models.Model):
    category_name=models.CharField(max_length=250,unique=True)
    def __str__(self):
        return self.category_name

"""author model for author details ie. author name"""
class Author(models.Model):
    author_name=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.author_name

"""bookmodel is for the details of book ie,name,price..."""
class Books(models.Model):
    book_name=models.CharField(max_length=200)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.IntegerField(default=50)
    pages=models.IntegerField(default=50)

    def __str__(self):
        return self.book_name

