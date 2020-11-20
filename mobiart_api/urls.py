from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/marketplace/', include("marketplace.urls")),
    path('api/profile/', include("profile_manager.urls")),
    path('api/auth/', include("auth.urls"))
]
