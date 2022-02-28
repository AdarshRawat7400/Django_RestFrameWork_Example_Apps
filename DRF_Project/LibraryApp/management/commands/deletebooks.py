from django.core.management.base import BaseCommand
from LibraryApp.models import Book

class Command(BaseCommand):
    help = 'Delete n number of books from Book table'
    def add_arguments(self,parser):
        parser.add_argument('number',type=int,help = 'Number of books to delete')
        
    def handle(self,*args,**kwargs):
        number = kwargs.get('number')
        for i in range(number):
            Book.objects.filter(id=i).delete()
        self.stdout.write(self.style.SUCCESS(f'{number} books deleted'))