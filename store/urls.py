from django.contrib import admin
from django.urls import path
from .views.home import IndexView, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('store/', store, name='store'),  # Updated URL pattern with a trailing slash
    path('signup/', Signup.as_view(), name='signup'),  # Added a trailing slash
    path('login/', Login.as_view(), name='login'),  # Added a trailing slash
    path('logout/', logout, name='logout'),  # Added a trailing slash
    path('cart/', auth_middleware(Cart.as_view()), name='cart'),  # Added a trailing slash
    path('checkout/', CheckOut.as_view(), name='checkout'),  # Added a trailing slash
    path('orders/', auth_middleware(OrderView.as_view()), name='orders'),  # Added a trailing slash
]
