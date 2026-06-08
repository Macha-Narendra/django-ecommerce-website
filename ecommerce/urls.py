from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from store import views_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views_auth.register, name='register'),
    path('store/', include('store.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
