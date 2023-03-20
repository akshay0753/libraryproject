"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import show_book, homepage,book_update,delete_book,softdelete,unavailable_book,available_book,login_page,register
urlpatterns = [
    path('admin/', admin.site.urls),
    path("show-book/",show_book , name="show-book"),
    path("home/", homepage ,name ="home"),
    path("book-update/<str:pk>", book_update ,name ="edit"),
    path("book-delete/<str:pk>", delete_book ,name ="delete"),
    path("unavailable/<str:pk>", softdelete ,name ="unavailable"),
    path("available/", available_book ,name ="available_book"),
    path("unavailable/",unavailable_book ,name ="unavailable_book"),
    path("login/",login_page,name="login"),
    path("register/",register,name="register"),

    
]
