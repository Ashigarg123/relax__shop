from django.shortcuts import render, redirect
from django.http import JsonResponse
from relax_n_shop.models import Product
from cart.models import Cart
from addresses.forms import AddressForm
from addresses.models import Address
from orders.models import Order
from billing.models import BillingProfile
# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    #total = 0
    #for x in products:
        #total+= x.Price
    print(products)
    #print(total)
    #cart_obj.total = total
    #cart_obj.save()
    print(cart_obj)
    return render(request, "cart/home.html", {"cart": cart_obj})


def cart_update(request):
    print("ASHI")
    product_id = request.POST.get('product_id')


    if product_id is not None:
        product_obj = Product.objects.get(id=product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            added=False
        else:
            cart_obj.products.add(product_obj)
            added=True
        request.session['cart_items'] = cart_obj.products.count()
        if request.is_ajax():
            print("It is ajax request")
            json_data={
            "added":added,
            "removed":not added,
            "cartItemCount":cart_obj.products.count(),

            }
            return JsonResponse(json_data)
    return redirect('product-detail',product_id)

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if  cart_obj.products.count()== 0:
        print(cart_created)
        print(cart_obj.products.count())
        return redirect('/products/')
    billing_profile,billing_profile_created= BillingProfile.objects.new_or_get(request)
    address_form=AddressForm()
    billing_address_form = AddressForm()
    billing_address_id=request.session.get("billing_address_id", None)
    shipping_address_id=request.session.get("shipping_address_id", None)
    address_qs=None
    #print(billing_profile_created)
    #print(billing_profile)
    #print(shipping_address_id)
    #print(billing_address_id)

    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs=Address.objects.filter(billing_profile=billing_profile)
            order_obj, order_obj_created = Order.objects.new_or_get(billing_profile,cart_obj)

        #shipping_address_qs=address_qs.filter(address_type='Shipping')
        #billing_address_qs=address_qs.filter(address_type='Billing')

        #print(order_obj_created)
        #billing_profile.save()
        if shipping_address_id:
            order_obj.shipping_address=Address.objects.get(id=shipping_address_id)
            #print(id)
            #print(shipping_address_id)
            del request.session['shipping_address_id']
            #print(billing_address_id)
            #print(shipping_address_id)
        if billing_address_id:
            order_obj.billing_address=Address.objects.get(id=billing_address_id)
            #print(billing_address_id)
            del request.session['billing_address_id']

        if billing_address_id or shipping_address_id:
            order_obj.save()
    if request.method =="POST":
        is_done=order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_items']=0
            del request.session['cart_id']
            return redirect("/checkout/success/")





    context = {
    "object": order_obj,
    "billing_profile":billing_profile,
    "address_form":address_form,
    "billing_address_form":billing_address_form,
    "address_qs":address_qs

    }


    return render(request, "cart/checkout.html", context)


def checkout_done_view(request):
    return render(request, "cart/checkout_done.html")
