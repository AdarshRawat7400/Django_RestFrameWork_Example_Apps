from django.core.management.base import BaseCommand
from LibraryApp.models import Book

class Command(BaseCommand):
    help = 'Show number of entries in the Book table and Schema'
    def handle(self,*args,**kwargs):
        schema = ''''''
        for field in Book._meta.fields:
            schema += f'{field.name} :  {field.get_internal_type()} \n'
            
        self.stdout.write(self.style.SUCCESS(f'Number of entries in Book table :- {Book.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Book Table Schema :- \n{schema}'))