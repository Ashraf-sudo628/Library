from django.shortcuts import redirect, render , get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
    
    context = {
        'categories': Category.objects.all(),
        'books' : Book.objects.all(),
        'forms' : BookForm(),
        'CatForm' :CategoryForm(),
        'allbooks' : Book.objects.filter(active = True).count(),
        'booksold' : Book.objects.filter(status = 'sold').count(),
        'bookrental' : Book.objects.filter(status = 'rental').count(),
        'bookavailable' : Book.objects.filter(status = 'available').count(),
        'bookunspecified' : Book.objects.filter(status = 'None').count(),

    }

    return render(request,'pages/index.html', context)

def books(request):
     
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    context = {
        'categories': Category.objects.all(),
        'books' : search,
        'CatForm' :CategoryForm(),
        
    }
     
    return render(request,'pages/books.html',context)

def update(request ,id):
    Book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST,request.FILES,instance=Book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:  
        book_save = BookForm(instance=Book_id)

    context = {
        'updated_book': book_save,
    }
    return render(request,'pages/update.html' , context)

def delete(request ,id):
    deleted_book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        deleted_book.delete()
        return redirect('/')
    
    return render(request,'pages/delete.html')