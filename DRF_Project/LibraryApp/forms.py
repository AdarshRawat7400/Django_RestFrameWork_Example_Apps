from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','author','price','description']

        labels = {
            'name':'Book Name',
            'author':'Author Name',
            'price':'Price',
            'description':'Description'
        }
