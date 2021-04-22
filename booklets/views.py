from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import BookletForm
from .models import Booklet,Isbn

def index(request):
    booklets = Booklet.objects.all()
    return render(request,"booklets/index.html",{
        "booklets" : booklets
    })

def show(request,id):
    booklet = Booklet.objects.get(pk=id)
    return render(request,"booklets/show.html",{
        "booklet" : booklet
    })


def create(request):
    #create instance from isbn b3d el form validation 
    form =  BookletForm(request.POST or None)
    if form.is_valid():
        form.save()
        # booklet = form.save()
        # booklet.isbn=Isbn.objects.create({
        # "booklet.author": author_title
        # })
        # booklet.save()
        return redirect ("index")
    return render (request,"booklets/create.html",{
        "form" : form
    })


def edit(request,id):
    booklet = Booklet.objects.get(pk=id)
    form =  BookletForm(request.POST or None,instance=booklet)
    if form.is_valid():
        form.save()
        return redirect ("index")
    return render (request,"booklets/edit.html",{
        "form" : form,
        "booklet" : booklet
    })


def delete(request,id):
    booklet = Booklet.objects.get(id=id)
    booklet.delete()
    return redirect ("index")
