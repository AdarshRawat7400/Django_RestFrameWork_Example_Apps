from django.core.management.base import BaseCommand
from LibraryApp.models import Book

class Command(BaseCommand):
    help = 'Add n number of books to Book table'
    def add_arguments(self,parser):
        parser.add_argument('number',type=int,help = 'Number of books to add')
        
    def handle(self,*args,**kwargs):
        number = kwargs.get('number')
        for i in range(number):
            Book.objects.create(
                name = f'Book {i}',
                author = f'Author {i}',
                price = i,
                description = f'Description {i}'
            )
        self.stdout.write(self.style.SUCCESS(f'{number} books added'))