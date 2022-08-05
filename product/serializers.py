from rest_framework import serializers
from .models import productsProductModel,produtsCategoryModel,productSubCategoryModel,productsBrandModel,productsAttributeModel,productsCartModel,productsOrderModel,productpaymentsModel
from django.contrib.auth import get_user_model
from accounts.serializers import accountUserListserializer

User = get_user_model()


class productsProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = productsProductModel
        fields = '__all__'

class produtsCtaegorySerializer(serializers.ModelSerializer):
    product = productsProductModelSerializer(read_only=True)

    class Meta:
        model = produtsCategoryModel
        fields = '__all__'

class produtsCategoryModelSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        serializer = produtsCtaegorySerializer(obj.product)
        return serializer.data

    class Meta:
        model = produtsCategoryModel
        fields = '__all__'





class produtsCategoryUpdateSerializer(serializers.ModelSerializer):
    product = productsProductModelSerializer(write_only=True)

    class Meta:
        model = produtsCategoryModel
        fields = '__all__'

    def update(self,instance,validated_data):
        product_data = validated_data.pop('product')
        product_serializer = productsProductModelSerializer(data=product_data,instance=instance.product,partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
        category_serializer = produtsCategoryModelSerializer(data=validated_data,instance=instance.category,partial=True)
        if category_serializer.is_valid():
            category_serializer.save()
        return instance


class productsBrandModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = productsBrandModel
        fields = '__all__'

class productSubCategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = productSubCategoryModel
        fields = '__all__'


class productsAttributeModelSerializer(serializers.ModelSerializer):

    product = productsProductModelSerializer(read_only=True)
    category = produtsCategoryModelSerializer(read_only=True)
    brand = productsBrandModelSerializer(read_only=True)
    sub_category = productSubCategoryModelSerializer(read_only=True)

    class Meta:
        model = productsAttributeModel
        fields = '__all__'

class productsCartModelSerializer(serializers.ModelSerializer):
    user = accountUserListserializer(read_only=True)
    product = productsAttributeModelSerializer(read_only=True)

    class Meta:
        model = productsCartModel
        fields = '__all__'

class productsOrderModelSerializer(serializers.ModelSerializer):
    user = accountUserListserializer(read_only=True)
    products = productsCartModelSerializer(read_only=True)

    class Meta:
        model = productsOrderModel

        fields = '__all__'



class productsAttributeCustomModelSerializer(serializers.ModelSerializer):

    product = productsProductModelSerializer(write_only=True)
    category = produtsCategoryModelSerializer(write_only=True)
    brand = productsBrandModelSerializer(write_only=True)
    sub_category = productSubCategoryModelSerializer(write_only=True)



    class Meta:
        model = productsAttributeModel
        fields = ['product','category','brand','sub_category','quantity','price']

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        productsProductModel.objects.create(**product_data)

        category_data = validated_data.pop('category')
        produtsCategoryModel.objects.create(**category_data)


        productsBrandModel_data = validated_data.pop('brand')
        productsBrandModel.objects.create(**productsBrandModel_data)



        productSubCategoryModel_data = validated_data.pop('sub_category')
        productSubCategoryModel.objects.create(**productSubCategoryModel_data)

        return validated_data


class produtsAttributeUpdateSerializer(serializers.ModelSerializer):
    product = productsProductModelSerializer(write_only=True,many= True)
    category = produtsCategoryModelSerializer(write_only=True)
    brand = productsBrandModelSerializer(write_only=True)
    sub_category = productSubCategoryModelSerializer(write_only=True)

    class Meta:
        model = productsAttributeModel
        fields = '__all__'

    def update(self, instance, validated_data):
        product_data = validated_data.pop('product')
        product_serializer = productsProductModelSerializer(data=product_data, instance=instance.product, partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
        category_data = validated_data.pop('category')
        category_serializer = produtsCategoryModelSerializer(data=category_data, instance=instance.category, partial=True)
        if category_serializer.is_valid():
            category_serializer.save()
        brand_data = validated_data.pop('brand')
        brand_serializer = productsBrandModelSerializer(data=brand_data, instance=instance.brand, partial=True)
        if brand_serializer.is_valid():
            brand_serializer.save()
        sub_category_serializer = productSubCategoryModelSerializer(data=validated_data, instance=instance.sub_category, partial=True)
        if sub_category_serializer.is_valid():
            sub_category_serializer.save()

        return instance


class productUserCartDetailSerializer(serializers.ModelSerializer):
    product = productsAttributeModelSerializer(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        serializer = accountUserListserializer(obj.user)
        return serializer.data
    class Meta:
        model = productsCartModel
        fields = '__all__'


class productsUsersOrderSerializer(serializers.ModelSerializer):
    products = productUserCartDetailSerializer(read_only=True)


    def get_user(self, obj):
        serializer = accountUserListserializer(obj.user)
        return serializer.data

    class Meta:
        model = productsOrderModel
        fields = '__all__'

class productUsersCartDetailSerializer(serializers.ModelSerializer):
    product = productsAttributeModelSerializer(read_only=True)
    user = accountUserListserializer(read_only=True)

    class Meta:
        model = productsCartModel
        fields = '__all__'


class paymentserailzer(serializers.ModelSerializer):
    user = accountUserListserializer(write_only=True)
    product = productsOrderModelSerializer(write_only=True,many=True)


    class Meta:

        model = productpaymentsModel


        fields = '__all__'




