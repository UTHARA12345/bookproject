from django.shortcuts import render,redirect
from consumer.forms import *
from consumer.models import *
from vendor.models import *
from vendor.views import bookView
# Create your views here.
def consumer_Reg(request):
    form=ConsumerRegForm()
    template_name="consumer/registration.html"
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form = ConsumerRegForm(request.POST)

        if form.is_valid():
            form.save()
            print("data saved")
            return redirect("clogin")
        else:
            return render(request, template_name, context)


    return  render(request,template_name,context)
def consumer_Login(request):
    form=ConsumerLoginForm()
    template_name="consumer/login.html"
    context={}
    context["form"]=form
    print("yes")
    if(request.method=="POST"):
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        data=Consumer.objects.all()
        print(uname)

        qs = Consumer.objects.get(username=uname)

        if ((uname == qs.username) & (pwd == qs.password)):
            print("login success")
            request.session["user"]=uname
            return redirect("consumerhome")
        else:
            return render(request, template_name, context)

    # if request.method=="POST":
    #     form=ConsumerLoginForm(request.POST)
    #     if(form.is_valid()):
    #         print("ok")
    #
    #         uname=form.cleaned_data["username"]
    #         pwd=form.cleaned_data["password"]
    return render(request,template_name, context)
def consumerHome(request):
    qs=Books.objects.all()
    context={}
    context["books"]=qs
    return render(request,"consumer/c_home.html",context)
def bView(request,pk):
    template_name="consumer/book_view.html"

    # return redirect(bookView(request,pk,template_name="consumer/book_view.html"))
    qs = Books.objects.get(id=pk)
    print(qs)

    context = {}
    context["book"] = qs
    return render(request, template_name, context)