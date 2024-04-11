from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        is_superuser = validated_data.pop('is_superuser', False)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if is_superuser:
            instance.is_superuser = True
        instance.save()
        return instance
