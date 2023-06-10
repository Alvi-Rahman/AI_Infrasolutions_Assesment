from django.urls import path
from geoservice.features.views import (FeatureListAPIView, FeatureRetrieveUpdateDestroyAPIView)

urlpatterns = [
    # path('list_features/', FeatureListView.as_view()),
    path('features/', FeatureListAPIView.as_view(), name='feature-list-create'),
    path('features/<int:id>/', FeatureRetrieveUpdateDestroyAPIView.as_view(),
         name='feature-retrieve-update-destroy'),
]
