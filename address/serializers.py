from rest_framework import serializers
from . models import User, Contact


class UserSerializer(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(
        view_name='contact_info',
        many=True,
        read_only=True
    )
    #####CUSTOM MAPPING
    user_url = serializers.ModelSerializer.serializer_url_field(view_name='user_info',)

    class Meta:
        model = User
        fields = ('id', 'user_name', 'user_email','user_password', 'contacts', 'user_url')
        

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    contact_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model= Contact
        fields = ['id', 'contact_user', 'contact_email', 'contact_first_name', 'contact_last_name', 'contact_phone_number',
        'contact_home_address', 'contact_age', 'contact_group', 'contact_relation', 'contact_notes']

    #     # contact_url = serializers.ModelSerializer.serializer_url_field(view_name='contact_info')'contact_url'
