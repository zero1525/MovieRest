from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from accounts.models import User
from django.conf import settings

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(email=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError["Неверный email или пароль"]
        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key, "email":user.email}
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password2")

        user = User.objects.create_user(
            password=password
            **validated_data
        )
        
        Token.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "full_name", "phone_number")
        read_only_fields = ("email",)


class FunctionChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, attrs):
        user = self.context['user']
        if not user.check_password(attrs.get('old_password')):
            raise serializers.ValidationError('Старый пароль неверный!')
        return attrs
    
    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class GenericChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, attrs):
        user = self.context["request"].user
        print(attrs.get("old_password"))
        if not user.checl_password(attrs.get("old_password")):
            raise serializers.ValidationError("Старый пароль неверен")
        return attrs
    
    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validate_data["new_password"])
        user.save()
        return user
    

class DeactivateAccountSerializer(serializers.Serializer):
    confirm = serializers.BooleanField

class SendMailSerilirzer(serializers.Serializer):
    to_email = serializers.EmailField()
    text = serializers.CharField()

    def create(self, validated_data):
        from django.core.mail import send_mail
        print('sent')
        send_mail(
            subject='Test Email',
            message = validated_data['text'],
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[validated_data['to_mail']],
            fail_silently=False
        )