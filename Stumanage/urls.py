from django.urls import path
from .views import *


urlpatterns = [
      path('manage/',manage,name ="manage"),
      path('form/',form,name ="form"),
      path('delete/<int:id>/',delete,name="delete"),
      path('activate/<int:id>/',activate,name="activate"),
      path('deactivate/<int:id>/',deactivate,name="deactivate"),
      path('register/',register,name="register"),
      path('',login,name="login"),
      path('logout/',logout,name="logout"),
      path('nav/',nav,name="nav"),
      path('inherit/',inherit,name="inherit"),
      path('update/<int:id>/',update,name="update"),

 ]
