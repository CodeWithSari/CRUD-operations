"""
URL configuration for SchoolEasy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from SchoolEasy_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name=""),
    path('admin_login', views.admin_login, name="admin_login"),
    path('register', views.register,name="register"),

    path('admin_logout',views.admin_logout,name="admin_logout"),


     # CRUD

    path('dashboard', views.dashboard, name="dashboard"),

    path('add_student', views.add_student, name="add_student"),


    path('student/update_student/<int:pk>', views.update_student, name='update_student'),

    path('student/<int:pk>', views.singular_student, name="student"),

    path('student/delete_student/<int:pk>', views.delete_student, name="delete_student"),


]
