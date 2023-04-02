from django.contrib import admin
from django.urls import path
from app import views
# from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('heartpage/', views.heartview, name='heartview'),
    path('strokepage/', views.strokeview, name='strokeview'),
    path('predictHeart/', views.predictHeart, name='predictHeart'),
    path('predictStoke/', views.predictStroke, name='predictStroke'),
    path('prescriptionpage/', views.prescriptionview, name='prescriptionview'),
    path('predictPrescription/', views.predictPrescription, name='predictPrescription'),
    path('lungpage/', views.lungview, name='lungview'),
    path('predictLung/', views.predictlung, name='predictlung'),
    path('diabetespage/', views.diabetesview, name='diabetesview'),
    path('predictDiabetes/', views.predictdiabetes, name='predictDiabetes'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

