from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blogs.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
