from django.conf import settings
from django.urls import re_path, path
from django.conf.urls import include, url
from django.contrib import admin
from main.urls import router
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny

urlpatterns = [
    url(r'^api/', include('main.urls')),
    re_path(r'^api/',  include(router.urls)),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account/', include('allauth.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    re_path("docs/", include_docs_urls(title='API Document', permission_classes=[AllowAny, ], authentication_classes=[])),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns