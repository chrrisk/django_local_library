from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # App URLs
    path('catalog/', include('catalog.urls')),  # keeps /catalog/ path working
    path('', include('catalog.urls')),          # ALSO map site root / to catalog
]

# Dev static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
