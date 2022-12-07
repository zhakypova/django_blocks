
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.block_list, name='block_list'),
    path('block/create/', views.block_create, name='block_create'),
    path('block/<int:id>/', views.block_detail, name='block_detail'),
    path('block/<int:id>/update', views.block_update, name='block_update'),
    path('block/<int:id>/delete', views.block_delete, name='block_delete'),
    path('apartment/list/', views.ApartmentListView.as_view(), name='apartment_list'),
    path('apartment/create/', views.ApartmentCreateView.as_view(), name='apartment_create'),
    path('apartment/<int:pk>/', views.ApartmentDetailView.as_view(), name='apartment_detail'),
    path('apartment/<int:pk>/update', views.ApartmentUpdateView.as_view(), name='apartment_update'),
    path('apartment/<int:pk>/delete', views.ApartmentDeleteView.as_view(), name='apartment_delete'),
]

