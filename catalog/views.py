from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status=2).count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits
    }
    return render(request, 'index.html', context)


class BookListView(ListView):
    model = Book
    paginate_by = 1


class BookDetailView(DetailView):
    model = Book
    slug_field = 'slug'


class AuthorListView(ListView):
    model = Author
    paginate_by = 1


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(
            borrower=self.request.user).filter(status__exact='2').order_by('due_back')
