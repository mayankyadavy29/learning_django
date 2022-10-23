from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

def index(request):
    book_list = Book.objects.all()
    context =  {
        'book_list': book_list
    }
    return render(request, 'myapp/index.html', context)

def detail(request, book_id):
    if request.method == 'POST':
        return redirect('/update', book_id=book_id)
    book = Book.objects.get(id=book_id)
    return render(request, 'myapp/detail.html',  {'book': book})

def add_book(request):
    if  request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        price = request.POST.get("price")
        book_image = request.FILES["book_image"]
        book = Book(name=name, desc=desc,  price=price, book_image=book_image)
        book.save()
    return render(request, 'myapp/add_book.html')

def update(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/update.html', {'form': form, 'book': book})

def delete(request, book_id):
    return render(request, 'myapp/delete.html', {'book_id': book_id})

def cnfrm_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/')