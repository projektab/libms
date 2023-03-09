from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from libms.models import Book


# Create your views here.
def add(request):
    if (request.method=='POST'):
        book_n = request.POST['bookn']
        author_n = request.POST['authorn']
        price_n = request.POST['price']
        type_n = request.POST['type']


        insert_data = Book.objects.create(bookn=book_n,authorn=author_n,price=price_n,type=type_n)
        insert_data.save()
        return redirect('/libms/main')

    return render(request,'add.html')

def index(request):
    content={}
    #content['data']=Task.objects.all()
    content['data']=Book.objects.filter(is_deleted='n')
    return render(request,'index.html',content)

def main(request):
    content={}
    #content['data']=Task.objects.all()
    content['data']=Book.objects.filter(is_deleted='n')
    return render(request,'main.html',content)


def userlogin(request):
    if request.method=="POST":
        af = AuthenticationForm(request=request, data=request.POST)
        #from django.contrib.auth.forms import AuthenticationForm
        if af.is_valid():
            uname = af.cleaned_data['username']
            upass = af.cleaned_data['password']
            is_authenticate = authenticate(username=uname,password=upass)
            #from django.contrib.auth import authenticate
            if is_authenticate:
                login(request,is_authenticate)
                messages.success(request,"login success")
                return redirect("/libms/main")
        else:
            messages.error(request,"login failed")
            return redirect("/")
    else:
        f=AuthenticationForm()
        content={}
        content['form']=f
        return render(request,"login.html",content)

def update(request,tid):
    if (request.method=='POST'):
        book_n = request.POST['bookn']
        author_n = request.POST['authorn']
        price_n = request.POST['price']
        type_n = request.POST['type']

        record_to_be_update = Book.objects.filter(id=tid)
        record_to_be_update.update(bookn=book_n,authorn=author_n,price=price_n,type=type_n)
        return redirect('/libms/main')
    else:
        content={}
        content['data'] = Book.objects.get(id=tid)
        return render(request,'update.html',content)

def delete(request,tid):
    record_to_be_deleted = Book.objects.filter(id=tid)
    #record_to_be_deleted.delete()
    record_to_be_deleted.update(is_deleted='y')
    return redirect('/libms/main')

def highToLow(request):
    content={}
    datas=Book.objects.order_by('-price')
    return render(request,'main.html',{'data':datas})

def lowToHigh(request):
    content={}
    datas=Book.objects.order_by('price')
    return render(request,'main.html',{'data':datas})


def authNatoz(request):
    content={}
    datas=Book.objects.order_by('authorn')
    return render(request,'main.html',{'data':datas})

def authNztoa(request):
    content={}
    datas=Book.objects.order_by('-authorn')
    return render(request,'main.html',{'data':datas})

def userlogout(request):
    logout(request)
    return redirect("/")
