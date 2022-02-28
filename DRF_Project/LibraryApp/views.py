from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .forms import BookForm
from django.views.generic.edit import (FormView,
                                       CreateView,
                                       UpdateView,
                                       DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
class HomeView( SuccessMessageMixin,TemplateView):
    template_name = 'LibraryApp/home.html'

    def get_success_message(self, cleaned_data=None):
        return "Welcome to Library App"
        

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['libraryname'] = 'SVVV Library'
        context['description'] = '''
                This is a library app it offers vast number of books and
                a wide range of books. that student can read and borrow '''

        return context

class HomeRedirectView(RedirectView):
    url = '/CBV_apis'



class BookListView(SuccessMessageMixin,ListView):
    model = Book
    success_message = "Welcome to Book List page"
    
    # template_name = 'LibraryApp/book_list.html' can be used to specify the template name
    ordering = ['price'] # default is '-id'
    # template_name_suffix = '_list' #this can be changed for changing the template name
    context_object_name = 'books' # default is object_list


    # Some Useful methods of ListView:

    # def get_queryset(self):  # this can be used to filter the data
    #     return Book.objects.filter(price__lte=300)

    # def get_context_data(self, **kwargs) : # this can be used to add extra data to the context
    #     context =  super().get_context_data(**kwargs)
    #     context['libraryname'] = 'SVVV Library'
    #     return context

    # def get_template_names(self):  // this can be used to change template based on type of user
    #     if self.request.user.is_superuser:
    #         template_name = 'LibraryApp/superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'LibraryApp/staff.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]



class BookDetailView(DetailView):
    model = Book
    # template_name = 'LibraryApp/bookdetail.html' # this can be used to specify the template name
    # context_object_name = 'book' # default is object name
    pk_url_kwarg = 'id' # default is 'pk'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['all_books'] = self.model.objects.all()
        return context


# class BookFormView(FormView):
#     template_name = 'LibraryApp/add_book_form.html'
#     form_class = BookForm
#     success_url = '/successfully_added/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#         # return HttpResponse('Successfully added') can be used to redirect to another page


class BookCreateView(CreateView):
    model = Book
    # form_class = BookForm   # can use your own form class or use the default one
    # template_name = 'LibraryApp/add_book_form.html' # can be used to specify template name explicitly otherwise it will be used as default
    fields = ['name','author','price','description']
    # success_url = '/successfully_added/' # another way to set get_absolute_url() in model class

    def get_form(self): # way to update form attributes
        form = super().get_form()
        form.fields['name'].widget.attrs.update({'class':'form-control'})
        form.fields['author'].widget.attrs.update({'class':'form-control'})
        form.fields['price'].widget.attrs.update({'class':'form-control'})
        form.fields['description'].widget.attrs.update({'class':'form-control'})
        return form





class BookUpdateView(UpdateView):
    model = Book
    fields = ['name','author','price','description']

    def get_form(self): # way to update form attributes
        form = super().get_form()
        form.fields['name'].widget.attrs.update({'class':'form-control'})
        form.fields['author'].widget.attrs.update({'class':'form-control'})
        form.fields['price'].widget.attrs.update({'class':'form-control'})
        form.fields['description'].widget.attrs.update({'class':'form-control'})
        return form


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/successfully_deleted/'
    template_name = 'LibraryApp/book_confirm_delete.html'

class SuccessfullyAddedView(TemplateView):
    template_name = 'LibraryApp/successfully_added.html'


class SuccessfullyDeletedView(TemplateView):
    template_name = 'LibraryApp/successfully_deleted.html'


