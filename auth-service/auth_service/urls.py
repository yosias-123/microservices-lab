from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 Incluir todas las rutas de tu app "users"
    path('api/', include('users.urls')),
]



