from django.conf import settings
from django.shortcuts import render, redirect

from billing.models import BillingProfile
from orders.models import Order
from products.models import Product
from accounts.forms import LoginForm,GuestForm
from .models import Cart

from accounts.models import GuestEmail


from addresses.forms import AddressForm
from addresses.models import Address

from billing.models import BillingProfile
from products.models import Product
from .models import Cart


def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	return render(request, "carts/home.html", {"cart": cart_obj})


def cart_update(request):
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Expired product")
			return redirect("cart:home")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)
		request.session['cart_items'] = cart_obj.products.count()
	return redirect("cart:home")

def checkout_home(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
		return redirect("cart:home")
	#user = request.user
	#billing_profile = None
	login_form = LoginForm()
	guest_form = GuestForm()
	address_form = AddressForm()
	
	billing_address_id = request.session.get("billing_address_id", None)

	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	address_qs = None

	if billing_profile is not None:
		if request.user.is_authenticated():
			address_qs = Address.objects.filter(billing_profile=billing_profile)
		order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
		if billing_address_id:
			order_obj.billing_address = Address.objects.get(id=billing_address_id) 
			del request.session["billing_address_id"]
		if billing_address_id:
			order_obj.save()

	if request.method == "POST":
		is_done = order_obj.check_done()
		if is_done:
			request.session['cart_items'] = 0
			del request.session['cart_id']
			return redirect("/cart/success")


	context = {
	     "object": order_obj,
	     "billing_profile": billing_profile,
	     "login_form" : login_form,
	     "guest_form" : guest_form,
	     "address_form": address_form,
	     "address_qs": address_qs,

	}
	return render(request, "carts/checkout.html", context)

def checkout_done_view(request):
    return render(request, "carts/checkout-done.html", {})


#def cart_create(user=None):
#	cart_obj = Cart.objects.create(user=None)
#	print('New Cart created')
#	return cart_obj


	#card_id = request.session.get("card_id", None)
	#if card_id is None:
	#	cart_obj = cart_create()
	#	request.session['card_id'] = cart_obj.id 
	#else:
	#qs = Cart.objects.filter(id=card_id)
	#if qs.count() == 1:
	#	print('Cart ID exists')
	#	cart_obj = qs.first()
	#	if request.user.is_authenticated() and cart_obj.user is None:
	#		cart_obj.user = request.user
	#		cart_obj.save()
	#else:
	#	cart_obj = Cart.objects.new(user=request.user)
	#	request.session['card_id'] = cart_obj.id

