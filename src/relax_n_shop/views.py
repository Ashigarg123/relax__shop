from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from cart.models import Cart

from .models import Product

class ProductListView(ListView):
    #paginate_by = 3
    model = Product
    #paginate_by = 3  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()

        si = self.request.GET.get("si")
        if si == None:

            si = ""


        object_list = Product.objects.filter(Q(title__icontains= si) | Q(category__icontains = si))
        context['object_list']=object_list
        return context

class ProductDetailView(DetailView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        context['now'] = timezone.now()
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context
