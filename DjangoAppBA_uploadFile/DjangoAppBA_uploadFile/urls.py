from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Urls der Django App mit einbinden
    path('fileUpload/', include('UploadFileApp.urls')),
]

# Nur bei Entwicklungsserver
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
