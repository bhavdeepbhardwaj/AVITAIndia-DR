from rest_framework import serializers
from .models import WarrantyRegistration


class WarrantyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarrantyRegistration
        fields = ("id", "user_id", "product_number_id", "serial_number", "reseller_name", "purchase_date",
                  "purchase_invoice")
