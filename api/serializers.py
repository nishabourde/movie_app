# api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Collection, Movie

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genres', 'uuid']

class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collection
        fields = ['id', 'title', 'description', 'movies']

# # api/serializers.py

# from django.contrib.auth.models import User
# from rest_framework import serializers, generics
# from .models import Collection, Movie
# # from rest_framework import generics
# # from .models import Collection
# from .serializers import CollectionSerializer

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password']
#         )
#         return user

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('title', 'description', 'genres', 'uuid')

# class CollectionSerializer(serializers.ModelSerializer):
#     movies = MovieSerializer(many=True)

#     class Meta:
#         model = Collection
#         fields = ('id', 'title', 'description', 'movies')
    
#     def create(self, validated_data):
#         movies_data = validated_data.pop('movies')
#         collection = Collection.objects.create(**validated_data)
#         for movie_data in movies_data:
#             Movie.objects.create(collection=collection, **movie_data)
#         return collection

#     def update(self, instance, validated_data):
#         movies_data = validated_data.pop('movies', None)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         if movies_data:
#             instance.movies.all().delete()
#             for movie_data in movies_data:
#                 Movie.objects.create(collection=instance, **movie_data)
#         return instance
    
# class CollectionListCreateView(generics.ListCreateAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class CollectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)