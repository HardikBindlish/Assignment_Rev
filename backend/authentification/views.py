from authentification.serializers import SignupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user

        content = {
            'message': ''
        }
        if user:
            content['message'] = user.username
        return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT token
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)

            response_data = {
                'message': 'User created successfully',
                'access': access_token,
                'refresh': str(refresh_token),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
