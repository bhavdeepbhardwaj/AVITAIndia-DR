from import_export.resources import ModelResource
from .models import WarrantyRegistration, WarrantyExtend, Certificate


#  Warranty Registration Import Export
class WarrantyRegistrationResources(ModelResource):
    class Meta:
        model = WarrantyRegistration
        import_id_fields = (
            'user_id', 'product_number_id', 'serial_number', 'reseller_name', 'purchase_date', 'purchase_invoice',)
        exclude = ('id', 'create_date', 'update_date',)


#  Warranty Extend Import Export
class WarrantyExtendResources(ModelResource):
    class Meta:
        model = WarrantyExtend
        import_id_fields = (
            'user_id', 'product_number_id', 'serial_number', 'reseller_name', 'purchase_date', 'purchase_invoice',)
        exclude = ('id', 'create_date', 'update_date',)


#  Certificate Import Export
class CertificateResources(ModelResource):
    class Meta:
        model = Certificate
        import_id_fields = (
            'user_id', 'order_id', 'product_configuration', 'product_number', 'serial_number', 'reseller_name',
            'purchase_date', 'extend_date')
        exclude = ('id', 'create_date', 'update_date',)
