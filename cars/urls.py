from django.urls import path
from .views import CarListView, CarCreateView, CarDetailView, CarUpdateView

app_name = 'cars'  # Убедитесь, что это указано для пространств имен

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='car_edit'),  # Убедитесь, что этот путь существует
]
