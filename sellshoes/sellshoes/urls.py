from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="SellShoes API",
        default_version="v1",
        description="An API for selling shoes",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ups.chime@gmail.com", name="Prince Chime"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/swagger.json", schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("test/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("accounts/", include("accounts.urls")),
]
