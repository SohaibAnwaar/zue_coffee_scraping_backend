from django.contrib import admin
from django.urls import path

from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


SPECTACULAR_SETTINGS = {
    'TITLE': 'Zue Coffee Shop API',
    'DESCRIPTION': 'Scrape the web for coffee shops',
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    'CAMELIZE_NAMES': False,
    'SERVE_PERMISSIONS': [],
    
    # OTHER SETTINGS
}

def hello_world_view(request):
    data = {'message': 'hello world'}

    return JsonResponse(data)


urlpatterns = [
    path('', hello_world_view),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
]
