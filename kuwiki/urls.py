from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from main.urls import router
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny
from main.views import PasswordResetView

urlpatterns = [
    path('api/', include('main.urls')),
    path('api/',  include(router.urls)),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path(' ', include('django.contrib.auth.urls')),
    path('password/reset/', PasswordResetView.as_view()),
    path("docs/", include_docs_urls(title='API Document', permission_classes=[AllowAny, ], authentication_classes=[])),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
