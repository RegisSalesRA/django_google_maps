from django.urls import path
from core.v1.views import CustomerViews,CustomerViewsCrud
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions



schema_view = get_schema_view(
   openapi.Info(
      title="Customers API",
      default_version='v1',
      description="Custormers objects from api google maps",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sales@gmail.com"),
      license=openapi.License(name="Sales License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('customers', CustomerViews.as_view()),
    path('customers/<int:pk>/', CustomerViewsCrud.as_view()),
    path('swagger_v1', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path("redoc", schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),

]