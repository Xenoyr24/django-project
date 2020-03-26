
from django.http import Http404, JsonResponse
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render

from billing.models import BillingProfile
from .models import Order, ProductPurchase




class OrderListView(ListView):

    def get_queryset(self):
        return Order.objects.by_request(self.request)

class OrderDetailView(DetailView):
    
    def get_object(self):
        qs = Order.objects.by_request(
                    self.request
                ).filter(
                    order_id = self.kwargs.get('order_id')
                )
        if qs.count() == 1:
            return qs.first()
        raise Http404
        



class LibraryView(ListView):
    template_name = 'orders/library.html'
    def get_queryset(self):
        return ProductPurchase.objects.products_by_request(self.request)


                #return Order.objects.get(id=self.kwargs.get('id'))
        #return Order.objects.get(slug=self.kwargs.get('slug'))
