from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from board import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('boards/', include('board.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)