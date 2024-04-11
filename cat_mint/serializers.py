from rest_framework import serializers

from .models import Cat, Image

class CatSerializer(serializers.ModelSerializer):
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.image_url  # Access related image's image_url

    image_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cat
        fields = (
            "id",
            "uuid",
            "cat_name",
            "description",
            "breed",
            "image_url",
            "owner",
            "created_at",
            "updated_at",
        )
        ordering = ['cat_name, breed, owner']

class CatSerializerCreation(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "id",
            "uuid",
            "image_url",
            "title",
        )                        
            