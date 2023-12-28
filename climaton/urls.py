from django.contrib import admin
from django.urls import path, include, re_path
from climaton import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(
        ('app.urls', 'app'),
        namespace='app'), 
    name='app'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)