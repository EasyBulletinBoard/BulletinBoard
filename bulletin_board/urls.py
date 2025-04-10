from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from board import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('boards/', include('board.urls')),
    path('account/', include('account.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)