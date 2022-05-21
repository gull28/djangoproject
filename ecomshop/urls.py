from django.urls import path
from . import views
from .views import account
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create", views.create, name="create"),
    path("view", views.view, name="view"),
    path("account", views.account, name="account"),
    path("shop",views.shop, name="shop"),
    path("contact", views.contact, name="contact"),
    path("staff", views.staff, name="staff")
]

urlpatterns+=staticfiles_urlpatterns()