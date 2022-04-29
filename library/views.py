from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import *
from django.http import request
from datetime import datetime, timedelta
from django.contrib import messages


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('library:home')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)




class UserLoginView(LoginView):
    template_name='library/login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('library:home')




class HomeView(LoginRequiredMixin, TemplateView):
    template_name='library/main.html'
    

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['accounts']=Account.objects.all()
        context['books'] = Book.objects.all()
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            #print(search_input)  
            context['books']=context['books'].filter(
                title__startswith=search_input)

        context['search_input']=search_input
        return context


class BookView(LoginRequiredMixin, ListView):
    model=Book
    context_object_name='books'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['books']=context['books']

        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['books']=context['books'].filter(
                title__startswith=search_input)

        context['search_input']=search_input

        return context



class BookCreate(LoginRequiredMixin, UserAccessMixin, CreateView):
    model=Book
    permission_required= 'books.add_books'
    fields='__all__'
    success_url=reverse_lazy('library:book-list')


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(BookCreate, self).form_valid(form)



class BookDetail(LoginRequiredMixin, DetailView):
    model=Book
    context_object_name='book'
    template_name='library/book.html'


    


class BookUpdate(LoginRequiredMixin,UserAccessMixin,  UpdateView):
    model=Book
    permission_required = 'books.change_books'
    fields='__all__'
    success_url=reverse_lazy('library:book-list')


class BookDelete(LoginRequiredMixin,UserAccessMixin,  DeleteView):
    model=Book
    permission_required = 'books.delete_book'
    context_object_name='book'
    fields='__all__'
    success_url=reverse_lazy('library:book-list')



class StudentView(LoginRequiredMixin, UserAccessMixin, ListView):
    model=Account
    context_object_name='students'
    permission_required = 'students.view_students'
    template_name='library/student_list.html'

    def get_context_data(self,  *args,**kwargs):
        context=super().get_context_data(**kwargs)
        context['students']=context['students'].exclude(is_admin=True)
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['students']=context['students'].filter(name__startswith=search_input)

        context['search_input']=search_input

        return context

class StudentDetail(LoginRequiredMixin, DetailView):
    model=Account
    context_object_name='student'
    template_name='library/student.html'




class StudentCreate(UserAccessMixin, CreateView):
    template_name = 'library/register.html'
    form_class = RegistrationForm
    permission_required = 'users.add_users'
    success_url = reverse_lazy('library:student-list')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(StudentCreate, self).form_valid(form)


class StudentUpdate(LoginRequiredMixin, UpdateView):
    form_class = AccountUpdateForm
    template_name = 'library/student_update.html'
    model = Account
    success_url=reverse_lazy('library:student-list')
    

    def form_valid(self, form):
        user = form.save()
        return super(StudentUpdate, self).form_valid(form)

class StudentDelete(LoginRequiredMixin,UserAccessMixin,  DeleteView):
    model=Account
    template_name = 'library/student_confirm_delete.html'
    permission_required = 'users.delete_users'
    context_object_name='student'
    fields='__all__'
    success_url=reverse_lazy('library:student-list')


