from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
# from

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('savollar', SavolAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('savollar_api/', SavolarAPIView.as_view()),
    path('savol_view/', SavolViews.as_view()),
    path('savollar_view/', SavollarViews.as_view()),
    path('savol/<int:pk>/javoblar/', Savol_JavoblariAPIView.as_view()),
    path('savol/<int:pk>/', SavolDetailView.as_view()),
    path('reaksiya/', ReaksiyaPOSTAPIView.as_view()),

    path('', include(router.urls)),

]
