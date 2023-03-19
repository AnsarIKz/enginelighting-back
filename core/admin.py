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


class ProductAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            # Получаем все категории без детей
            categories = Category.objects.filter(children__isnull=True)
            # Устанавливаем ограничения для поля категории
            kwargs["queryset"] = categories
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Images
admin.site.register(Post, PostAdmin)
admin.site.register(Useful, UsefulAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(Request)
admin.site.register(Category)
admin.site.register(Review)
