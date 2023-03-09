from django.urls import path
from libms import views


urlpatterns = [
    path('add/', views.add),
    path('index/', views.index),
    path('main/', views.main),
    path("login/", views.userlogin),
    path('delete/<int:tid>',views.delete),
    path('update/<int:tid>',views.update),
    path('htol',views.highToLow),
    path('ltoh',views.lowToHigh),
    path('auatz',views.authNatoz),
    path('auzta',views.authNztoa),
    path('logout', views.userlogout),


]
