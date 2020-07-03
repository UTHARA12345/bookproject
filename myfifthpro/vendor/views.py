from django.shortcuts import render,redirect
from vendor.forms import BookCreateFrm,BookAuthor,BookCategory,BookUpdate,AuthorUpdate,CategoryUpdate
from vendor.models import Books,Category,Author

def getHome(request):
    return render(request,"index.html")
def book_create(request):
    form=BookCreateFrm()
    template_name="book_create.html"
    context={}
    context["form"]=form
    if(request.method=="POST"):
        form=BookCreateFrm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("listbook")

            #we have to specify the redirect

    return render(request,template_name,context)
def list_book(request):
    template_name="list_book.html"
    querySet=Books.objects.all()
    context={}
    context["qs"]=querySet
    return render(request,template_name,context)
def BAuthor(request):
    form=BookAuthor()
    template_name="book_author.html"
    context={}
    context["form"]=form
    if(request.method=="POST"):
        form=BookAuthor(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("listauthor")
        else:
            form=BookAuthor(request.POST)
            context={}
            context["form"] = form
            return render(request, template_name, context)
    return render(request, template_name, context)
def list_Author(request):
    template_name="list_author.html"
    querySet=Author.objects.all()
    context={}
    context["qs"]=querySet
    return render(request,template_name,context)
def BCategory(request):
    form=BookCategory()
    template_name="book_category.html"
    context={}
    context["form"]=form
    if(request.method=="POST"):
        form=BookCategory(request.POST)
        if(form.is_valid()):
            form.save()

            return redirect("listcategory")
        else:
            form=BookCategory(request.POST)
            context={}
            context["form"] = form
            return render(request, template_name, context)
    return render(request, template_name, context)
def list_category(request):
    template_name="list_category.html"
    querySet=Category.objects.all()
    context={}
    context["qs"]=querySet
    return render(request,template_name,context)
def bookView(request,pk,template_name="book_view.html"):


    qs=Books.objects.get(id=pk)
    print(qs)

    context = {}
    context["book"]=qs
    return render(request,template_name,context)
def delete_Book(request,pk):
    qs=Books.objects.get(id=pk).delete()
    context={}
    context["book"]=qs
    return redirect("listbook")
def bookView_Author(request,pk):
    temp_name="book_author_view.html"
    qs=Author.objects.get(id=pk)
    print(qs)
    context={}
    context["author"]=qs
    return render(request, temp_name, context)
def delete_Author(request,pk):
    qs=Author.objects.get(id=pk).delete()
    context={}
    context["author"]=qs
    return redirect("listauthor")
def bookView_Category(request,pk):
    temp_name="book_category_view.html"
    qs=Category.objects.get(id=pk)
    print(qs)
    context={}
    context["category"]=qs
    return render(request, temp_name, context)
def delete_Category(request,pk):
    qs=Category.objects.get(id=pk).delete()
    context={}
    context["category"]=qs
    return redirect("listcategory")
def update_Book(request,pk):
    qs=Books.objects.get(id=pk)
    form=BookUpdate(instance=qs)
    template_name="update_book.html"
    context={}
    context["form"]=form
    if(request.method=="POST"):
        form=BookUpdate(request.POST)
        if(form.is_valid()):
            bname=form.cleaned_data["book_name"]
            cname = form.cleaned_data["category_name"]
            aname=form.cleaned_data["author"]
            prc = form.cleaned_data["price"]
            pages=form.cleaned_data["pages"]
            qs.book_name=bname
            qs.category_name=cname
            qs.author=aname
            qs.price=prc
            qs.pages=pages
            qs.save()

            return redirect("listbook")
    return render(request,template_name,context)
def update_Author(request,pk):
    qs=Author.objects.get(id=pk)
    form=AuthorUpdate(instance=qs)
    template_name="update_author.html"
    context={}
    context["form"]=form
    if(request.method == "POST"):
        form=AuthorUpdate(request.POST)
        if(form.is_valid()):
            aname = form.cleaned_data["author_name"]
            qs.author_name=aname
            qs.save()
            return redirect("listauthor")
    return render(request,template_name,context)
def Update_Category(request,pk):
    qs=Category.objects.get(id=pk)
    form=CategoryUpdate(instance=qs)
    template_name="update_category.html"
    context={}
    context["form"]=form
    if(request.method=="POST"):
        form=CategoryUpdate(request.POST)
        if(form.is_valid()):
            cname=form.cleaned_data["category_name"]
            qs.category_name=cname
            qs.save()
            return redirect("listcategory")
    return render(request,template_name,context)