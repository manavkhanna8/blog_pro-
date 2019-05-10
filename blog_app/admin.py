from django.contrib import admin
from blog_app.models import Post,Comment

# Register your models here.
# admin.site.register(Post) # if you want to register only model to the admin interface or want all the fields

class Postadmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status',]
    prepopulated_fields={'slug':('title',)}#this field is used to populate field according to other field
    list_filter=('status','author','title')# this is used to filter according to the parameter we pass e.g we want posts according to the title
    search_fields=('title','body','status')# this is used to search something in fields according to word given
    raw_id_fields=('author',)# when you wnat to search in database stored values acc to key
    ordering=['status','publish']# this is used to sort
    date_hierarchy='publish'#this is used to show the hierarchy in top in the form of navbar
class Commentadmin(admin.ModelAdmin):
    list_display=('name','email','body','post','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Post,Postadmin)#this line is used to regiter model to the admin if you have some customization in admin
admin.site.register(Comment,Commentadmin)
