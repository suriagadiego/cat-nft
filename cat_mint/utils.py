from rest_framework_simplejwt.tokens import UntypedToken

def get_user_info_from_jwt(token):
  try:
    decoded_token = UntypedToken(token)
    user_id = decoded_token['user_id']
    print("======"*10)
    print(user_id.first_name)
    print("======"*10)
    return user_id  # Or return the specific user information you need
  except (UntypedToken.InvalidToken, UntypedToken.ExpiredToken):
    return None  # Handle invalid or expired tokens
