from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("profile_edit/", views.profile_edit, name="profile_edit"),
    path("password_edit/", views.password_edit, name="password_edit"),
    path("register/", views.register, name="register"),
    path("medicijnen/", views.medicijnen, name="medicijnen"),
    path("medicijnen/<str:pk>", views.medicijnen_edit, name="medicijnen"),
    path("medicijnendelete/<str:pk>", views.medicijn_delete, name="medicijnendelete"),
    path("afhaalactie/", views.afhaalactie, name="afhaalactie"),
    path("afhaalactiedelete/<str:pk>", views.afhaalactie_delete, name="afhaalactiedelete"),
    path("afhaalactie_afhalen/<str:pk>", views.afhaalactie_afhalen, name="afhaalactie_afhalen"),
    path("afhaalactie_aproven/<str:pk>", views.afhaalactie_aproven, name="afhaalactie_aproven"),
]