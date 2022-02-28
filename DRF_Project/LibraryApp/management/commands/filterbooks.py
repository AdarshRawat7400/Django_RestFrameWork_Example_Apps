from django.core.management.base import BaseCommand
from LibraryApp.models import Book


class Command(BaseCommand):
    help = 'Filter books by price'
    def add_arguments(self,parser):
        parser.add_argument('price',type=int,help = 'Price to filter')
        parser.add_argument('filename',type=str,help = 'File to save')
        
    def handle(self,*args,**kwargs):
        price = kwargs.get('price')
        filename = kwargs.get('filename')
        books = Book.objects.filter(price__lte=price)
    
        with open(filename+'.txt','w') as f:
            for book in books:
                f.write(f'{book.name},{book.author},{book.price},{book.description}\n')
        self.stdout.write(self.style.SUCCESS(f'{len(books)} entries saved in filename :- {filename}.txt saved'))