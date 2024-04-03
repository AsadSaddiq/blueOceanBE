from rest_framework import serializers
from .models import Property, Amenity, Rating, PropertyImage

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['name']

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'value']

class PropertySerializer(serializers.ModelSerializer):
    amenities = AmenitySerializer(many=True)
    # ratings = RatingSerializer(many=True)
    property_images = PropertyImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields="__all__"
        # fields = [
        #     'id', 'owner', 'title', 'description', 'property_type', 'bedrooms', 'bathrooms', 'area',
        #     'city', 'neighborhood', 'address', 'rent_amount', 'currency', 'available_from', 'is_featured',
        #     'amenities', 'contact_name', 'contact_email', 'contact_phone', 'created_at', 'updated_at',
        #     'floor_number', 'is_furnished', 'is_pet_friendly', 'heating_system', 'cooling_system',
        #     'parking_spaces', 'is_security_system', 'property_images', 'average_rating',
        # ]

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        total_ratings = sum([rating.value for rating in ratings]) if ratings else 0
        return round(total_ratings / len(ratings), 2) if len(ratings) > 0 else 0
