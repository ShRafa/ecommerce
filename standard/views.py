import datetime
import json
from decimal import Decimal
from typing import Any, Dict

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.models import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import *
from .utils import cartData, cookieCart, guestOrder


def store(request):
    data = cartData(request)
    cartItems = data["cartItems"]

    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    return render(request, "standard/store.html", context)


def cart(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    order = data["order"]
    items = data["items"]

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "standard/cart.html", context)


def checkout(request):
    data = cartData(request)
    cartItems = data["cartItems"]
    order = data["order"]
    items = data["items"]

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "standard/checkout.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]

    print("Action:", action)
    print("productId:", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, _ = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = Decimal(data["form"]["total"])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data["shipping"]["address"],
            city=data["shipping"]["city"],
            state=data["shipping"]["state"],
            zipcode=data["shipping"]["zipcode"],
        )

    return JsonResponse("Payment complete", safe=False)


def historic(request):
    if request.user.is_authenticated:
        # orders = Order.objects.filter(customer=request.user)
        orders = Order.objects.all()
        return render(request, "standard/historic.html", {'orders':orders})
    else:
        return redirect("login")
    
class SigninView(CreateView):
    template_name = "standard/signin.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("store")

    def form_valid(self, form):
        user = form.save()
        if user:
            Customer.objects.create(user=user, name=user.username, email='')
            login(self.request, user)

        return super(SigninView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("store")
        return super().get(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    template_name = "standard/logout.html"


class UserLoginView(LoginView):
    template_name = "standard/login.html"
    redirect_authenticated_user = True
    request = None

    def get_success_url(self):
        return reverse_lazy("store")
    
    # def get_context_data(self, **kwargs):
    #     context = cartData(self.request)
    #     return context
