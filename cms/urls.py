
from django.contrib import admin
from django.urls import path
from servers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name="addandshow"),
    path('addserver/', views.addserver, name="addserver"),
    path('showserver/', views.showserver, name="showserver"),

    path('delete/<int:id>/',views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutuser, name="logout"),

]
