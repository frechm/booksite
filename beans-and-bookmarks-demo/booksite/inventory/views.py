from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from .models import Book
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'inventory/index.html'

class SearchResultsView(ListView):
    model = Book
    template_name = 'inventory/book_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Book.objects.filter(Q(title__icontains=query) | Q(isbn__icontains=query))

        return object_list
        context = {
            'query' : query,
        }
    

