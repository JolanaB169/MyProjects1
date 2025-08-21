from django.shortcuts import render, get_object_or_404
from Books.models import Genre, Book

def book_list(request):
    genre_id = request.GET.get('genre')
    genres = Genre.objects.all()
    books = Book.objects.all()

    if genre_id:
        books = books.filter(genre__id=genre_id)

    context = {
        'books': books,
        'genres': genres,
        'selected_genre': int(genre_id) if genre_id else None
    }

    return render(request, 'book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})