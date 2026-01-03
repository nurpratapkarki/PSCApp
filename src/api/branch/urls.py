from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.branch.views import BranchViewSet, CategoryViewSet, SubBranchViewSet

router = DefaultRouter()
router.register(r"branches", BranchViewSet)
router.register(r"sub-branches", SubBranchViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
