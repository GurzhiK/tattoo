from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('prices/', include('prices.urls')),
    path('api/', include('artists.urls')),
    path('api/', include('photos.urls')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
