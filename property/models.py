from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Amenity(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class PropertyImage(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='property_images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"{self.property.title} - Image"

class Rating(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.property.title} - {self.user.email} - {self.value} stars"

class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('condo', 'Condo'),
        # Add more property types as needed
    ]

    BEDROOM_CHOICES = [(i, f'{i} Bedroom') for i in range(1, 9)]
    BED_CHOICES = [(i, f'{i} Bed') for i in range(1, 12)]

   

    HEATING_CHOICES = [
        ('central', 'Central Heating'),
        ('electric', 'Electric Heating'),
        ('gas', 'Gas Heating'),
        # Add more heating options as needed
    ]

    COOLING_CHOICES = [
        ('central', 'Central Cooling'),
        ('split', 'Split System Cooling'),
        # Add more cooling options as needed
    ]
    TIME_CHOICES = [
        ('day', 'DAY'),
        ('month', 'MONTH'),
        ('year', 'YEAR'),
        # Add more cooling options as needed
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    purpose = models.CharField(max_length=20)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    bedrooms = models.IntegerField(choices=BEDROOM_CHOICES, validators=[MinValueValidator(1)])
    bed = models.IntegerField(choices=BED_CHOICES, validators=[MinValueValidator(1)])
    bathrooms = models.IntegerField(validators=[MinValueValidator(1)])
    area = models.DecimalField(max_digits=8, decimal_places=2)  # in square meters
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    rent_period = models.CharField(max_length=20, choices=TIME_CHOICES)
    currency = models.CharField(max_length=3, default='USD')  # Use appropriate currency code
    available_from = models.DateField(validators=[MinValueValidator(limit_value=timezone.now().date())])
    is_featured = models.BooleanField(default=False)
    amenities = models.ManyToManyField(Amenity, blank=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    floor_number = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    is_furnished = models.BooleanField(default=False)
    heating_system = models.CharField(max_length=20, choices=HEATING_CHOICES, blank=True, null=True)
    cooling_system = models.CharField(max_length=20, choices=COOLING_CHOICES, blank=True, null=True)
    parking_spaces = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    is_security_system = models.BooleanField(default=False)

    def average_rating(self):
        ratings = self.ratings.all()
        total_ratings = sum([rating.value for rating in ratings]) if ratings else 0
        return round(total_ratings / len(ratings), 2) if len(ratings) > 0 else 0

    def __str__(self):
        return self.title
