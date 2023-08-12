from django.urls import path

from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("process_order/", views.processOrder, name="process_order"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("signin/", views.SigninView.as_view(), name="signin"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("historic/", views.historic, name="historic"),
    path(
        "product_profile/<int:product_id>/",
        views.productProfile,
        name="product_profile",
    ),
]
