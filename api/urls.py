# api/urls.py

from django.urls import path
from .views import (
    RegisterView, MovieListView, CollectionListCreateView, 
    CollectionRetrieveUpdateDestroyView, request_count_view, reset_request_count_view
)
from .views import CustomTokenObtainPairView
urlpatterns = [
    # path('', api_root_view, name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('collection/', CollectionListCreateView.as_view(), name='collection-list-create'),
    path('collection/<uuid>/', CollectionRetrieveUpdateDestroyView.as_view(), name='collection-detail'),
    path('request-count/', request_count_view, name='request-count'),
    path('request-count/reset/', reset_request_count_view, name='request-count-reset'),
]


# # api/urls.py

# from django.urls import path
# from .views import RegisterView
# from .views import RegisterView, MovieListView, CollectionListCreateView, CollectionRetrieveUpdateDestroyView, request_count_view, reset_request_count_view

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('movies/', MovieListView.as_view(), name='movie-list'),
#     path('collection/', CollectionListCreateView.as_view(), name='collection-list-create'),
#     path('collection/<uuid>/', CollectionRetrieveUpdateDestroyView.as_view(), name='collection-detail'),
#     path('request-count/', request_count_view, name='request-count'),
#     path('request-count/reset/', reset_request_count_view, name='request-count-reset'),
# ]
