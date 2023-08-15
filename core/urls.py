from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from book import router as boor_router
from users import router as users_router


api_auth_urlpatterns = []

api_urlpatterns = [
    path(r'auth/', include(api_auth_urlpatterns)),
    path(r'books/', include(boor_router.router.urls)),
    path(r'users/', include(users_router.router.urls)),
]

if settings.DEBUG:
    api_urlpatterns.append(
        path(r'verify/', include('rest_framework.urls'))
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]
