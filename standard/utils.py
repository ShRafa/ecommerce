import json

from django.contrib.auth.models import User

from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES["cart"])
    except:
        cart = {}

    print("Cart:", cart)
    items = []
    order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
    cartItems = order["get_cart_items"]

    for itemCart in cart:
        try:
            cartItems += cart[itemCart]["quantity"]

            product = Product.objects.get(id=int(itemCart))
            total = product.price * cart[itemCart]["quantity"]

            order["get_cart_total"] += total
            order["get_cart_items"] += cart[itemCart]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "imageURL": product.imageURL,
                },
                "quantity": cart[itemCart]["quantity"],
                "get_total": total,
            }
            items.append(item)

            if product.digital == False:
                order["shipping"] = True
        except:
            pass

    return {"cartItems": cartItems, "order": order, "items": items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData["cartItems"]
        order = cookieData["order"]
        items = cookieData["items"]

    return {"cartItems": cartItems, "order": order, "items": items}


def productDetails(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product

    except Product.DoesNotExist:
        return None


def guestOrder(request, data):
    print("Usuário não cadastrado...")

    print("COOKIES:", request.COOKIES)
    name = data["form"]["name"]
    email = data["form"]["email"]
    password = data["form"]["password"]
    password_confirm = data["form"]["password_confirm"]

    cookieData = cookieCart(request)
    items = cookieData["items"]

    if Customer.objects.filter(email=email).exists():
        customer = Customer.objects.get(email=email)
    else:
        password_match = password == password_confirm

        if not password_match:
            raise ValueError("Senhas não coincidem")

        user = User.objects.create(username=name, email=email, password=password)
        customer = Customer.objects.create(email=email, user=user)

    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item["product"]["id"])

        OrderItem.objects.create(
            product=product, order=order, quantity=item["quantity"]
        )
    return customer, order
