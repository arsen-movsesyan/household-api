from passman import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=True)

router.register(r'person', views.PersonViewSet, basename='person')
router.register(r'address', views.AddressViewSet, basename='address'),
router.register(r'vehicle', views.VehicleViewSet, basename='vehicle'),
router.register(r'person-document', views.PersonDocumentViewSet, basename='person-document'),
router.register(r'account', views.AccountViewSet, basename='account'),
router.register(r'recurring-account', views.RecurringAccountViewSet, basename='recurring-account'),

urlpatterns = router.urls
