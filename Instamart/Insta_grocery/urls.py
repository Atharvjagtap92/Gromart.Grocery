from django.conf import settings 
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("update_data/<int:id>", views.update_data, name="update_data"),
    path("delete_data/<int:id>", views.delete_data, name="delete_data"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)