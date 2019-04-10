from django.shortcuts import render
from .models import Books
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .forms import CreateBook
# Create your views here.
def book_list(request):
    books = Books.objects.filter(published_date__lt=timezone.now()).order_by('-published_date')
    return render(request, 'books.html', {'books': books})

def book_new(request):
    if request.method == "POST":
        form = CreateBook(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.published_date = timezone.now()
            book.save()
            return redirect('book_list')
    else:
        form = CreateBook()
        return render(request, 'postBook.html', {'form': form})
def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.user == book.user:
        book.delete()
        return redirect('book_list')
    else:
        return redirect('book_list')
