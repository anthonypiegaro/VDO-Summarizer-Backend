from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "confirm_password")

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        user.save()
        return user
