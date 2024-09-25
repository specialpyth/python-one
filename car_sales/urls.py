from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import car_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', car_list, name='car_list'),  # Главная страница
    path('', include(('cars.urls', 'cars'), namespace='cars')),  # Подключаем маршруты cars
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
