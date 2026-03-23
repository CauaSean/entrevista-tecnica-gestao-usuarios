from people import views

# ViewSet class based views
from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register('people', views.PersonViewSet)
router.register('checkins', views.CheckinViewSet)
router.register('patient_companion_checkin',
                views.PatientCompanionCheckinViewSet)
router.register('home_services', views.HomeServicesViewSet)
router.register('professional_services', views.ProfessionalServicesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    #Swagger/OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # router.register('checkins', views.CheckinViewSet)
    path('api/', include(router.urls)),
]


