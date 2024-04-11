from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..models import Cat
from ..serializers import CatSerializer, CatSerializerCreation
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination


def custom_permission_classes(permissions):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                # If the user is not authenticated, return a custom error response
                return Response({"error": True, "detail": "Authentication credentials were not provided."}, status=401)
            elif not request.user.is_superuser:
                # If the user is not an admin user, return a custom error response
                return Response({"error": True, "detail": "You do not have permission to perform this action."}, status=403)
            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator


# @permission_classes([IsAuthenticated])
@api_view(["GET"])
# @custom_permission_classes([IsAuthenticated, IsAdminUser])
def list_all_cats(request):
    cats = Cat.objects.all()
    sort_by = request.GET.get('sort_by', None)
    cat_name_filter = request.GET.get('cat_name', None)
    breed_filter = request.GET.get('breed', None)
    owner_filter = request.GET.get('owner', None)

    if cat_name_filter:
        cats = cats.filter(cat_name__icontains=cat_name_filter)

    if breed_filter:
        cats = cats.filter(breed__icontains=breed_filter)
    
    if owner_filter:
        cats = cats.filter(owner__icontains=owner_filter)

    if sort_by:
        cats = cats.order_by(sort_by)

    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(cats, request)
    serializer = CatSerializer(page if page is not None else cats, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def list_cats_by_owner(request):
    cats = Cat.objects.filter(owner=request.user.id)
    sort_by = request.GET.get('sort_by', None)
    cat_name_filter = request.GET.get('cat_name', None)
    breed_filter = request.GET.get('breed', None)

    if cat_name_filter:
        cats = cats.filter(cat_name__icontains=cat_name_filter)

    if breed_filter:
        cats = cats.filter(breed__icontains=breed_filter)
    
    if sort_by:
        cats = cats.order_by(sort_by)

    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(cats, request)
    serializer = CatSerializer(page if page is not None else cats, many=True)
    return paginator.get_paginated_response(serializer.data)