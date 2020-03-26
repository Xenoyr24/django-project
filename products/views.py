from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from carts.views import Cart
from .models import Product




class ProductFeaturedDetailView(DetailView):
	queryset = Product.objects.featured()
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()



class ProductListView(ListView): 
	template_name = "products/list.html"


    #def get_context_data(self, *args, **kwargs):
	#	context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
	#	print(context)
		#context['abc'] = 123
	#	return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()


#def product_list_view(request):
#	queryset = Product.objects.all()
#
#	context = {
#	      'object_list' : queryset
#	}
#	return render(request, "products/list.html", context)


class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		print(context)
	#	context['cart']   = cart_obj
		return context 

	def get_object(self, *args, **kwargs):
		request  = self.request
		slug       = self.kwargs.get('slug')
		#instance = get_object_or_404(Product, slug=slug, active=True)
		try: 
			instance = Product.objects.get(slug=slug, active=True)
		except Product.DoesNotExist:
			raise Http404("Not found..")
		except Product.MultipleObjectsReturned:
			queryset = Product.objects.filter(slug=slug, active=True)
			instance = qs.first()
		except:
			raise Http404("uhm...")
		return instance

 


class ProductDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		#context['abc'] = 123
		return context


	def get_object(self, *args, **kwargs):
		request  = self.request
		pk       = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product doesn't exist")
		return instance

		#def get_queryset(self, *args, **kwargs):
		#request = self.request
		#pk = self.kwargs.get('pk')
		#return Product.objects.filter(pk=pk)

def product_detail_view(request, pk=None, *args, **kargs ):
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist")

	context = {
	'object': instance
	}

	return render(request, "products/detail.html", context)
	#queryset = Product.objects.get(pk=pk)
	#instance = get_object_or_404(product, pk=pk)
    # try:
   
    #  except Product.DoesNotExist:
    #  	print ('no product here')
    #  	raise Http404("Product doesn't exist")
    #  except:
    #  	print("huh?")

      	#print(instance)
  	#qs = Product.objects.filter(id=pk)
    
    #print(qs)
    #if qs.count() == 1:
    #	instance = qs.first()
    #else:
    #	raise Http404("Product DoesNotExist")



