from django.contrib import admin
from . import models
# Register your models here.

class InformationAdmin(admin.StackedInline):
    model = models.Information


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')
    inlines = [InformationAdmin]
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug' , 'parent')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Size)
admin.site.register(models.Color)
