from authenticationApp.models import User, User_Profile
from home.models import UserChatbotSocket
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers


class UserProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = ['id', 'user_email', 'user_address', 'user_name_bn', 'user_NID_no', 'user_organization', 'location', 'district', 'division']

class UserSerializer(serializers.ModelSerializer):
    # user_profile = UserProfileSerailizer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'first_name', 'last_name']


class UserChatbotSocketSerializer(serializers.ModelSerializer):
    chatbot_socket_created_at = serializers.DateTimeField(source="created_at")
    class Meta:
        model = UserChatbotSocket
        fields = ['chatbot_socket_id', 'registered_user_session_uuid', 'chatbot_socket_created_at']
