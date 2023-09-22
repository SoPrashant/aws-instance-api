from rest_framework import serializers
from login_credentials_api.models import CloudLogin

class CloudLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudLogin
        fields = ['email_address','account_id', 'access_key', 'secret_key']
