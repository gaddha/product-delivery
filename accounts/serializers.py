from rest_framework import serializers
from .models import User
from product.models import productsCartModel
class accountUserListserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'


class accountsUserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','dob','gender','password']

    def validate(self,attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User with  email already exists")

        return super().validate(attrs)

    def create(self,validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            dob=validated_data['dob'],
            gender=validated_data['gender'],
        )
        user.set_password(validated_data['password'])
        user.save()
        productsCartModel.objects.create(user=user)#create cart as user creatad
        return user



class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'dob', 'gender')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            }
    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(email=value).exists():
    #         raise serializers.ValidationError({"email": "This email is already in use."})
    #     return value

    # def validate_username(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(username=value).exists():
    #         raise serializers.ValidationError({"username": "This username is already in use."})
    #     return value

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.dob = validated_data['dob']
        instance.gender = validated_data['gender']
        instance.save()

        return instance


