import datetime
import json
from decimal import Decimal

from django import forms
from django.contrib.auth import login, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView

from .models import *
from .utils import cartData, guestOrder


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


@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        try:
            customer, order = guestOrder(request, data)
        except:
            raise ValueError("Senhas não coincidem")

    total = Decimal(data["form"]["total"].replace(",", "."))
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

    login(request, customer.user)

    return JsonResponse("Payment complete", safe=False)


def historic(request):
    if request.user.is_authenticated:
        orders = request.user.customer.order_set.order_by("-id", "complete")
        return render(request, "standard/historic.html", {"orders": orders})
    else:
        return redirect("login")


username_validator = UnicodeUsernameValidator()


class SigninForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=12,
        min_length=4,
        required=True,
        help_text="Nome necessário",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=12,
        min_length=4,
        required=True,
        help_text="Sobrenome necessário",
        widget=(forms.TextInput(attrs={"class": "form-control"})),
    )
    email = forms.EmailField(
        max_length=50,
        help_text="E-mail necessário",
        widget=(forms.TextInput(attrs={"class": "form-control"})),
    )
    password1 = forms.CharField(
        label=_("Senha"),
        widget=(forms.PasswordInput(attrs={"class": "form-control"})),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Confirmar senha"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        help_text=_("Senhas não coincidem"),
    )
    username = forms.CharField(
        label=_("Username"),
        max_length=150,
        help_text=_("Máximo de 150 caracteres. Letras, dígistos e apenas @/./+/-/_ ."),
        validators=[username_validator],
        error_messages={"unique": _("Usuário já existe.")},
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class SigninView(CreateView):
    template_name = "standard/signin.html"
    form_class = SigninForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        if user:
            Customer.objects.create(user=user, name=user.username, email=user.email)
            # login(self.request, user)

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
