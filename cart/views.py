from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    return render(request, "cart_summary.html", {})


def cart_add(request):
    
    # Get the carret
    cart = Cart(request)
    
    #test for POST 
    
    if request.POST.get('action') == 'post':
        #Gettting stuff
        product_id = int(request.POST.get('product_id'))
        #look prodcut in DB
        product = get_object_or_404(Product, id=product_id)
        
        
        # save to session
        cart.add(product = product)
        
        #get cart Quantity
        cart_quantity = cart.__len__()
        
        # Return response
        # response = JsonResponse({'Product Name:': product.name})
        response = JsonResponse({'qty:': cart_quantity})
        return response
    
    

def cart_delete(request):
    pass

def cart_update(request):
    pass