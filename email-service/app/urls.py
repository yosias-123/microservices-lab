from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.notifications.views import ContactViewSet, NotifyViewSet

router = DefaultRouter()
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'notify', NotifyViewSet, basename='notify')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
