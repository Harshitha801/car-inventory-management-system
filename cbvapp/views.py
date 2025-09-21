from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from cbvapp.models import Company,Products
from django.urls import reverse_lazy
# Create your views here.
# class className(View):
#     def get(self,request):
#         return HttpResponse("<h1>This is class based views</h1>")
class Myclass(TemplateView):
    template_name="home.html"
class AllCompanies(ListView):
    model=Company
class CompanyDetails(DetailView):
    model=Company
    context_object_name="mycompanies"
class AddNewCompany(CreateView):
    model=Company
    fields='__all__'
class CompanyUpdate(UpdateView):
    model=Company
    fields=['name','ceo','logo']
class CompanyDelete(DeleteView):
    model=Company
    success_url=reverse_lazy('list')
