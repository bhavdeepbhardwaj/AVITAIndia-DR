from django.shortcuts import render
from requests import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import WarrantyRegistration
from .serializers import WarrantyRegistrationSerializer


def homePage(request):
    return render(request, "index.html")


# LIST ALL GET
class WarrantyRegistrationList(ListAPIView):
    queryset = WarrantyRegistration.objects.all()
    serializer_class = WarrantyRegistrationSerializer


# Create POST
class CreateWarrantyRegistration(CreateAPIView):
    serializer_class = WarrantyRegistrationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateWarrantyRegistration(RetrieveUpdateAPIView):
    queryset = WarrantyRegistration.objects.all()
    serializer_class = WarrantyRegistrationSerializer


class DeleteWarrantyRegistration(DestroyAPIView):
    queryset = WarrantyRegistration.objects.all()
    serializer_class = WarrantyRegistrationSerializer
