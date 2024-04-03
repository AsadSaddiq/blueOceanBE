from django.urls import path
from .views import PropertyList, PropertyDetail, PropertyImages, rate_property

urlpatterns = [
    path('properties/', PropertyList.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
    # path('properties/<int:pk>/images/', PropertyImages.as_view(), name='property-images'),
    path('properties/images/', PropertyImages.as_view(), name='allProperty-images'),
    path('properties/<int:property_id>/rate/', rate_property, name='rate-property'),
    # Add more paths for additional functionality if needed
]
