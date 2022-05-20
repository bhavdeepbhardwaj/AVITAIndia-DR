from rest_framework import serializers
from .models import WarrantyRegistration, WarrantyExtend, Certificate


class WarrantyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarrantyRegistration
        fields = ("id", "user_id", "product_number_id", "serial_number", "reseller_name", "purchase_date",
                  "purchase_invoice")


class WarrantyExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarrantyExtend
        fields = ("id", "user_id", "product_number_id", "serial_number", "reseller_name", "purchase_date",
                  "purchase_invoice")


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ("id", "user_id", "order_id", "product_configuration", "product_number", "serial_number",
                  "reseller_name", "purchase_date", "extend_date")
