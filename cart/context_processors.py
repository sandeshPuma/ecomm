from .cart import Cart

# create context processoe so our cart can work on all pages


def cart(request):
    # Return the default data
    return{'cart': Cart(request)}