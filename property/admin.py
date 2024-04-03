from django.contrib import admin
from .models import Property, Amenity, PropertyImage, Rating

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'bedrooms', 'bathrooms', 'rent_amount', 'is_featured')
    list_filter = ('property_type', 'bedrooms', 'is_featured')
    search_fields = ['title', 'description', 'city', 'owner__username']
    inlines = [PropertyImageInline, RatingInline]

class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('property', 'user', 'value')

admin.site.register(Property, PropertyAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
admin.site.register(Rating, RatingAdmin)
