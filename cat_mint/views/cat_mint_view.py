from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import Cat
from ..serializers import (
    CatSerializer, ImageSerializer, CatSerializerCreation
)

import cloudinary.uploader
import cloudinary

# from ..nftminting import mint_nft

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def register_cat(request):
    cat_info = request.data.copy() 
    # cat_info = request.data
    cat_info['owner'] = request.user.id
    image_pk = upload_image(request)
    cat_info['image'] = image_pk

    serializer = CatSerializerCreation(data=cat_info)
    if serializer.is_valid():
        serializer.save()

        cat_id = serializer.data["id"]
        cat = Cat.objects.filter(id=cat_id).first()
        cat_serializer = CatSerializer(cat, many=False)
    
        return Response(cat_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def upload_image(request):

    print('=='*10)
    print(request.data)

    title = f"{request.user.first_name}'s {request.data['breed']} cat named {request.data['cat_name']}"
    image_url = request.data['image_url']
    # if image_url:
    #     uploaded_image = cloudinary.uploader.upload(image, public_id=f'{request.data["cat_name"]}_{request.user.first_name}_{request.user.id}')
    #     image_url = uploaded_image['url']

    image_data = {
            "image_url": image_url,
            "title": title
    }

    image_serializer = ImageSerializer(data=image_data)
    if image_serializer.is_valid():
        image_saved = image_serializer.save()
        image_pk = image_saved.pk

    return image_pk