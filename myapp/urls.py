from django.urls import path
from .views import View,Register,Category,Addproduct
from myapp import views
urlpatterns=[
    path('',View.as_view()),
    path('pro/<str:addcategory>/',views.View2),
    path('wish/',views.View3),
    path('car/',views.cart),
    path('cadd/', views.cadd),
    path('reg/',views.userreg),
    path('log/',views.userlogin),
    path('cat/',views.Addcat),
    #path('addgro/<str:addcategory>/', views.Proadd),
    path('addpro/<str:addcategory>/',views.Addgrocery),
    path('prodetail/<int:id>/',views.Prodetail),
    path('checkout/', views.Checkout),
    path('urs/', views.useraddress),
    path('stkupd/', views.stockupdation),

]