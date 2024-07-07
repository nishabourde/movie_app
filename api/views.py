# api/views.py

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Collection
from rest_framework import generics
from django.http import HttpResponse
from .serializers import UserSerializer, MovieSerializer, CollectionSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# from rest_framework.views import APIView
# from rest_framework.response import Response
from .utils import fetch_movies

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        response.data['access_token'] = str(refresh.access_token)
        return response

@api_view(['GET'])
def home_view(request):
    return HttpResponse("Welcome to the Movie Collection API!")
# class RegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             return Response(
#                 {'access_token': str(refresh.access_token)},
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        page = request.query_params.get('page', 1)
        movies = fetch_movies(page)
        return Response(movies)

class CollectionListCreateView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CollectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    # This is just a wrapper to use the default TokenObtainPairView
    pass

@api_view(['GET'])
def request_count_view(request):
    count = cache.get('request_count', 0)
    return Response({'requests': count})

@api_view(['POST'])
def reset_request_count_view(request):
    cache.set('request_count', 0, None)
    return Response({'message': 'request count reset successfully'})