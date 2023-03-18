from django.contrib import admin
from .models import PostPhoto, Post, UsefulPhoto, Useful, Request, Category, Review, Project, ProjectPhoto, Product
# Register your models here.


class PostPhotoInline(admin.TabularInline):
    model = PostPhoto


class PostAdmin(admin.ModelAdmin):
    inlines = [PostPhotoInline]


class UsefulPhotoInline(admin.TabularInline):
    model = UsefulPhoto


class UsefulAdmin(admin.ModelAdmin):
    inlines = [UsefulPhotoInline]


class ProjectPhotoInline(admin.TabularInline):
    model = ProjectPhoto


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectPhotoInline]


# Images
admin.site.register(Post, PostAdmin)
admin.site.register(Useful, UsefulAdmin)

admin.site.register(Request)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Product)
