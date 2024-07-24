from api import views
from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("product", views.ProductViewSet, basename="product")

urlpatterns = [path("", include(router.urls))]
