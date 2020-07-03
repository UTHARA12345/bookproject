from django.forms import ModelForm
from vendor.models import Books,Author,Category

class BookCreateFrm(ModelForm):
    class Meta:
        model=Books

        fields=["book_name","category_name","author","price","pages"]

    def clean(self):
        print("inside clean")

class BookAuthor(ModelForm):
    class Meta:
        model=Author

        fields=["author_name"]

    def clean(self):
        cleaned_data=super().clean()
        name=cleaned_data.get("author_name")
        ob=Author.objects.filter(author_name=name)
        if(ob):
            self.add_error("author_name","this author is already exist")

        print("inside clean author")


class BookCategory(ModelForm):
    class Meta:
        model=Category
        fields=["category_name"]

    def clean(self):
        cleaned_data = super().clean()
        name=cleaned_data.get("category_name")
        ob=Category.objects.filter(category_name=name)
        if(ob):
            self.add_error("category_name", "this author is already exist")
        print("inside clean category")
class BookUpdate(ModelForm):
    class Meta:
        model=Books
        fields="__all__"
    def clean(self):
        print("inside clean update")
class AuthorUpdate(ModelForm):
    class Meta:
        model=Author
        fields="__all__"
    def clean(self):
        print("insie clean author")
class CategoryUpdate(ModelForm):
    class Meta:
        model=Category
        fields="__all__"
    def clean(self):
        print("clean category")