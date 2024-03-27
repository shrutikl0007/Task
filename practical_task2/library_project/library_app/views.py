from django.shortcuts import redirect
from django.shortcuts import render
from .models import BookRequest, Book
from .models import Book
from django.shortcuts import render, redirect
from .models import Book, BookRequest


def home(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, "home.html", context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'your_username' and password == 'your_password':
           
            return redirect('home')
        else:
            
            context = {'error_message': 'Invalid username or password'}
            return render(request, 'login.html', context)
    return render(request, 'login.html')


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        stock = int(request.POST.get('stock'))
        status = request.POST.get('status') == 'True'

        book = Book(title=title, author=author, stock=stock, status=status)
        book.save()

        return redirect('view_books')

    return render(request, "add_book.html")


def approve_requests(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')

        book_request = BookRequest.objects.get(id=request_id)

        if action == 'approve':
          
            book_request.approved = True
            book_request.save()

            book = Book.objects.get(id=book_request.book_id)
            book.status = False
            book.save()

        elif action == 'reject':
            
            book_request.approved = False
            book_request.save()

            book = Book.objects.get(id=book_request.book_id)
            book.status = True
            book.save()

        return redirect('approve_requests')

    requests = BookRequest.objects.all()
    context = {
        "requests": requests
    }
    return render(request, "approve_requests.html", context)


def view_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "view_books.html", context)


def logout(request):
    return redirect('home')
