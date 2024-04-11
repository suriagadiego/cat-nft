from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import Cat
from ..serializers import (
    CatSerializer,
)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_cat(request, cat_uuid):
    cat = Cat.objects.filter(uuid=cat_uuid).first()

    if cat is None:
        return Response({"error": "Cat not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.user.id != cat.owner_id:
        return Response({"error": "Unauthorized request"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
