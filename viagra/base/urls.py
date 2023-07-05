from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path("medicijnen/", views.medicijnen, name="medicijnen"),
    path("medicijnen/<str:pk>", views.medicijnen_edit, name="medicijnen"),
    path("medicijnendelete/<str:pk>", views.medicijn_delete, name="medicijnendelete"),
    path("afhaalactie/", views.afhaalactie, name="afhaalactie"),
    path("afhaalactiedelete/<str:pk>", views.afhaalactie_delete, name="afhaalactiedelete"),
]