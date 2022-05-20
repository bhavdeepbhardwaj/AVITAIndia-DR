from . import views
from django.urls import path

urlpatterns = [
    # URL API Warranty Registration
    path('warranty-registration/', views.WarrantyRegistrationList.as_view(),
         name='Warranty Registration List'),
    path('warranty-registration/create', views.CreateWarrantyRegistration.as_view(),
         name='Warranty Registration Create'),
    path('warranty-registration/<int:pk>/', views.UpdateWarrantyRegistration.as_view(),
         name='Warranty Registration Update'),
    path('warranty-registration/<int:pk>/delete', views.DeleteWarrantyRegistration.as_view()),

    # URL API Warranty Extend
    path('warranty-extend/', views.WarrantyExtendList.as_view(),
         name='Warranty Extend List'),
    path('warranty-extend/create', views.CreateWarrantyExtend.as_view(),
         name='Warranty Extend Create'),
    path('warranty-extend/<int:pk>/', views.UpdateWarrantyExtend.as_view(),
         name='Warranty Extend Update'),
    path('warranty-extend/<int:pk>/delete', views.DeleteWarrantyExtend.as_view()),

    # URL API Certificate
    path('certificate/', views.CertificateList.as_view(),
         name='Certificate List'),
    path('certificate/create', views.CreateCertificate.as_view(),
         name='Certificate Create'),
    path('certificate/<int:pk>/', views.UpdateCertificate.as_view(),
         name='Certificate Update'),
    path('certificate/<int:pk>/delete', views.DeleteCertificate.as_view()),
]
