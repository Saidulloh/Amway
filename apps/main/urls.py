from rest_framework.routers import DefaultRouter

from apps.main.views import MainApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=MainApiViewSet
)

urlpatterns = router.urls
