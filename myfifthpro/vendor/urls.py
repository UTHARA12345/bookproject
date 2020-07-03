"""myfifthpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vendor.views import getHome,book_create,list_book,BAuthor,BCategory,list_Author,list_category,bookView,delete_Book,bookView_Author,delete_Author,bookView_Category,delete_Category,update_Book,update_Author,Update_Category

urlpatterns = [
    path('',getHome,name="vhome"),
    path('bookcreate',book_create,name="createbook"),
    path('listbook',list_book,name="listbook"),
    path('bauthor',BAuthor,name="bookauthor"),
    path('bcategory',BCategory,name="bookcategory"),
    path('listauthor',list_Author,name="listauthor"),
    path('listcategory',list_category,name="listcategory"),
    path('viewbook/<int:pk>',bookView,name="viewbook"),
    path('deletebook/<int:pk>',delete_Book,name="deletebook"),
    path('viewauthor/<int:pk>',bookView_Author,name="viewauthor"),
    path('deleteauthor/<int:pk>',delete_Author,name="deleteauthor"),
    path('viewcategory/<int:pk>', bookView_Category, name="viewcategory"),
    path('deletecategory/<int:pk>', delete_Category, name="deletecategory"),
    path('updatebook/<int:pk>',update_Book,name="updatebook"),
    path('updateauthor/<int:pk>',update_Author,name="updateauthor"),
    path('updatecategory/<int:pk>',Update_Category,name="updatecategory"),
]
