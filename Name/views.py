from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def home(request):
    books = Book.objects.all()
    
    return render(request, 'Name/Name.html',{

        'books' : books
    }) 



