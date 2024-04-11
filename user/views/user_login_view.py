from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from ..models import CustomUser
import jwt, datetime


@api_view(['POST'])
def login_user(request):

    if request.method != 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    email = request.data['email']
    password = request.data['password']

    user = CustomUser.objects.filter(email=email).first()

    if user is None:
        raise AuthenticationFailed("User not Found")

    if not user.check_password(password):
        raise AuthenticationFailed("Incorrect Password")
    
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow(),
    }
    
    token = jwt.encode(payload, 'secret', algorithm='HS256')

    return Response({
        "jwt": token
    })