from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('', admin.site.urls),
]

if settings.DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__', include(debug_toolbar.urls)),
                  ] + urlpatterns

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
