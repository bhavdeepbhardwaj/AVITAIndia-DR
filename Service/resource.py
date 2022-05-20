from import_export.resources import ModelResource
from .models import ServiceCenter, WhereToBuy


#  Service Center Import Export
class ServiceCenterResources(ModelResource):
    class Meta:
        model = ServiceCenter
        import_id_fields = ('shop_Name', 'locale', 'country', 'address', 'opening_hour', 'phone', 'email', 'city',
                            'state', 'pin', 'latitude', 'longitude')
        exclude = ('id', 'create_date', 'update_date',)


#  Where To Buy Import Export
class WhereToBuyResources(ModelResource):
    class Meta:
        model = WhereToBuy
        import_id_fields = ('shop_Name', 'locale', 'country', 'address', 'opening_hour', 'phone', 'email', 'city',
                            'state', 'pin', 'latitude', 'longitude')
        exclude = ('id', 'create_date', 'update_date',)
