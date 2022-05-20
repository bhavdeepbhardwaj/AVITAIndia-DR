from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import WarrantyRegistration, WarrantyExtend, Certificate
from .serializers import WarrantyRegistrationSerializer, WarrantyExtendSerializer, CertificateSerializer


def homePage(request):
    return render(request, "index.html")


#  Warranty Registration
# LIST ALL GET
class WarrantyRegistrationList(ListAPIView):
    queryset = WarrantyRegistration.objects.all()
    serializer_class = WarrantyRegistrationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'serial_number']
    search_fields = ['serial_number']


# Create POST
class CreateWarrantyRegistration(CreateAPIView):
    serializer_class = WarrantyRegistrationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#  Update PUT
class UpdateWarrantyRegistration(RetrieveUpdateAPIView):
    queryset = WarrantyRegistration.objects.all()
    serializer_class = WarrantyRegistrationSerializer


# Delete DELETE
class DeleteWarrantyRegistration(DestroyAPIView):
    queryset = WarrantyRegistration.objects.all()
    serializer_class = WarrantyRegistrationSerializer


# Warranty Extend
# LIST ALL GET
class WarrantyExtendList(ListAPIView):
    queryset = WarrantyExtend.objects.all()
    serializer_class = WarrantyExtendSerializer


# Create POST
class CreateWarrantyExtend(CreateAPIView):
    serializer_class = WarrantyExtendSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#  Update PUT
class UpdateWarrantyExtend(RetrieveUpdateAPIView):
    queryset = WarrantyExtend.objects.all()
    serializer_class = WarrantyExtendSerializer


# Delete DELETE
class DeleteWarrantyExtend(DestroyAPIView):
    queryset = WarrantyExtend.objects.all()
    serializer_class = WarrantyExtendSerializer


# Certificate
# LIST ALL GET
class CertificateList(ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


# Create POST
class CreateCertificate(CreateAPIView):
    serializer_class = CertificateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#  Update PUT
class UpdateCertificate(RetrieveUpdateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


# Delete DELETE
class DeleteCertificate(DestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
