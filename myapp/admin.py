from django.contrib import admin
from .models import Register,Category,Addproduct,tCart,sales,salessub,address
class AdminLogin(admin.ModelAdmin):
    list_display = ('uname','pword','rights')
    search_fields = ('uname','pword')

class Categoryadmin(admin.ModelAdmin):
    list_display = ('addcategory',)

class Productadmin(admin.ModelAdmin):
    list_display = ('productname',)
class cartadmin(admin.ModelAdmin):
    list_display = ('orderno','serialno','pid','pname','quantity','rate','total')
class salesadmin(admin.ModelAdmin):
    list_display = ('salesno','sdate','custid','cname','total','cardno','expdate','ccv','carduser')
class salessubadmin(admin.ModelAdmin):
    list_display = ('salesno','productid','pname','quantity','rate','total')
class addressadmin(admin.ModelAdmin):
    list_display=('fname','lname','country','staddress','town','state','pin','ph','email')


admin.site.register(Addproduct,Productadmin)
admin.site.register(Category,Categoryadmin)
admin.site.register(Register,AdminLogin)
admin.site.register(tCart,cartadmin)
admin.site.register(sales,salesadmin)
admin.site.register(salessub,salessubadmin)
admin.site.register(address,addressadmin)