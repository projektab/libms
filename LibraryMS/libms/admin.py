from django.contrib import admin
from libms.models import Book

# Register your models here.

class PriceFilter(admin.SimpleListFilter):
    title='Price Filter'
    parameter_name='Price Filter'
    def lookups(self,request,model_admin):
        return(('htol','Price High to Low'),('ltoh','Price Low to High'))
    def queryset(self,request,queryset):
        if(self.value()=='htol'):
            return queryset.order_by('-price')
        elif(self.value()=='ltoh'):
            return queryset.order_by('price')
        else:
            return queryset.all()

class AuthornaFilter(admin.SimpleListFilter):
    title='Authorna Filter'
    parameter_name='Authorna Filter'
    def lookups(self,request,model_admin):
        return(('auatz','Author A to Z'),('auzta','Author Z to A'))
    def queryset(self,request,queryset):
        if(self.value()=='auatz'):
            return queryset.order_by('-authorn')
        elif(self.value()=='auzta'):
            return queryset.order_by('authorn')
        else:
            return queryset.all()

class Bookadmin(admin.ModelAdmin):
    list_display=['id','bookn','authorn','price','type','is_deleted']
    list_filter=[PriceFilter,AuthornaFilter]

admin.site.register(Book,Bookadmin)
