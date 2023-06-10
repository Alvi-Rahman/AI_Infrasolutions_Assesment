from django.urls import path

from geoservice.frontend_views.views import *

urlpatterns = [
    path('', login_view, name='login-view'),
    path('map/', map_view, name='map-view'),
    path('features_list/', feature_list_view, name='feature-list'),
    path('features_edit/<int:pk>', feature_edit_view, name='feature-edit'),
]
