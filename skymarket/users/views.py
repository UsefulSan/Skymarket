from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

from users.serializers import UserSerializer
import requests


class UserActivationView(APIView):
    def get(self, request, uid, token):
        protocol = 'https://' + request.is_secure()
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/users/activate/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        content = result.text
        return Response(content)
