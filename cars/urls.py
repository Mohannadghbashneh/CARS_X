from django.urls import path
from .views import CarListView,CarDetailView,CarCreateView,CarUpdateView,CarDeleteView 

urlpatterns=[
    path('car/',CarListView.as_view(),name='car_list'),
    path('car/<int:pk>/',CarDetailView.as_view(),name='car_detail'),
    path('car/create/',CarCreateView.as_view(),name="car_create"),
    path ('car/<int:pk>/update/',CarUpdateView.as_view(),name='car_update'),
    path('car/<int:pk>/delete/',CarDeleteView.as_view(),name='car_delete')
]