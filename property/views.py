from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from .models import Property,PropertyImage, Rating, Amenity
from .serializers import PropertySerializer, RatingSerializer, AmenitySerializer,PropertyImageSerializer

class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print("Debug - PropertyDetail view - serialized data:", serializer.data)
        return Response(serializer.data)


@api_view(['POST'])
def rate_property(request, property_id):
    try:
        property_instance = Property.objects.get(pk=property_id)
    except Property.DoesNotExist:
        return Response({'error': 'Property not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(property=property_instance, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyImages(APIView):
#   permission_classes = [IsAuthenticated]
  def post(self, request, pk, format=None):
    serializer = PropertyImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

  def get(self, request, pk=None, format=None):
    serializer = PropertyImageSerializer(data=request.data)
    id = pk
    if id is not None:
      stu = PropertyImage.objects.filter(id=id)
      serializer = PropertyImageSerializer(stu, many=True)
      return Response(serializer.data)
    stu = PropertyImage.objects.all()
    serializer = PropertyImageSerializer(stu, many=True)
    return Response(serializer.data)
    
