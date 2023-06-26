from django.shortcuts import render, redirect
from store.models.product import Products
from django.views import View

class Cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        ids = list(cart.keys())
        products = []

        try:
            if ids:
                products = Products.get_products_by_id(ids)
        except Exception as e:
            print(f"An error occurred while retrieving products: {e}")

        return render(request, 'cart.html', {'products': products})
