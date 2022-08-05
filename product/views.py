from django.shortcuts import render
from .models import *
from . import serializers
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class productsLsitCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productsProductModel.objects.all()
    serializer_class = serializers.productsProductModelSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.productsProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class prdocutsProductGetViews(APIView):

    def get(self, request,slug, *args, **kwargs):
        product = productsProductModel.objects.filter(slug=slug)
        serializer = serializers.productsProductModelSerializer(product, many=True)
        return Response(serializer.data)

class prdocutsProductUpdateViews(APIView):

    def put(self, request, slug, format=None):
        product = productsProductModel.objects.get(slug = slug)
        serializer = serializers.productsProductModelSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class prdocutsProductDeleteViews(APIView):
    def delete(self, request, slug, format=None):
        product = productsProductModel.objects.get(slug=slug)
        product.delete()
        return Response({'msg': 'deleted successfully'})
# ___________________________________________________________________________________________________________________________________________________________________________________________________


class productsCategoryLsitCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = produtsCategoryModel.objects.all()
    serializer_class = serializers.produtsCategoryModelSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.produtsCategoryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class prdocutsCategoryGetViews(APIView):

    def get(self, request,slug, *args, **kwargs):
        category = produtsCategoryModel.objects.filter(slug=slug)
        serializer = serializers.produtsCategoryModelSerializer(category, many=True)
        return Response(serializer.data)

class prodcutsCategoryUpdateView(APIView):

    def put(self, request, slug, format=None):
        print(request.data)
        category = produtsCategoryModel.objects.get(slug=slug)
        serializer = serializers.produtsCategoryUpdateSerializer(data=request.data,instance=category,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class productsCategoryDeleteView(APIView):
    def delete(self, request, slug, format=None):
        product = productsProductModel.objects.get(slug=slug)
        product.delete()
        return Response({'msg': 'deleted successfully'})

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class productsBrandModelsLsitCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productsBrandModel.objects.all()
    serializer_class = serializers.productsBrandModelSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.productsBrandModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class prdocutsBrandGetViews(APIView):

    def get(self, request, slug, *args, **kwargs):
        brand = productsBrandModel.objects.filter(slug=slug)
        serializer = serializers.productsBrandModelSerializer(brand, many=True)
        return Response(serializer.data)


class prodcutsBrandUpdateView(APIView):

    def put(self, request, slug, format=None):
        print(request.data)
        brand = productsBrandModel.objects.get(slug=slug)
        serializer = serializers.productsBrandModelSerializer(data=request.data, instance=brand, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsBrandDeleteView(APIView):
    def delete(self, request, slug, format=None):
        brand = productsBrandModel.objects.get(slug=slug)
        brand.delete()
        return Response({'msg': 'deleted successfully'})

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class productsSubCategoryLsitCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productSubCategoryModel.objects.all()
    serializer_class = serializers.productSubCategoryModelSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.productsBrandModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class prdocutSubCategoryGetViews(APIView):

    def get(self, request, slug, *args, **kwargs):
        SubCategory = productSubCategoryModel.objects.filter(slug=slug)
        serializer = serializers.productSubCategoryModelSerializer(SubCategory, many=True)
        return Response(serializer.data)


class prodcutsSubCategoryUpdateView(APIView):

    def put(self, request, slug, format=None):
        print(request.data)
        SubCategory = productSubCategoryModel.objects.get(slug=slug)
        serializer = serializers.productSubCategoryModelSerializer(data=request.data, instance=SubCategory, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsSubCategoryDeleteView(APIView):
    def delete(self, request, slug, format=None):
        SubCategory = productSubCategoryModel.objects.get(slug=slug)
        SubCategory.delete()
        return Response({'msg': 'deleted successfully'})

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class productsAttributeModelLsitCreateView(generics.ListAPIView):
    queryset = productsAttributeModel.objects.all()
    serializer_class = serializers.productsAttributeModelSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)



class productsAttributeModelCustomCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productsAttributeModel.objects.all()
    serializer_class = serializers.productsAttributeCustomModelSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request, *args, **kwargs):
        serializer = serializers.productsAttributeCustomModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class prdocutAttributeModelGetViews(APIView):

    def get(self, request, slug, *args, **kwargs):
        attribute = productsAttributeModel.objects.filter(slug=slug)
        serializer = serializers.productsAttributeModelSerializer(attribute, many=True)
        return Response(serializer.data)


class prodcutsAttributeModelUpdateView(APIView):

    def put(self, request, slug, format=None):
        print(request.data)
        attribute = productsAttributeModel.objects.get(slug=slug)
        serializer = serializers.productsAttributeCustomModelSerializer(data=request.data, instance=attribute, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsAttributeModelDeleteView(APIView):
    def delete(self, request, slug, format=None):
        attribute = productsAttributeModel.objects.get(slug=slug)
        attribute.delete()
        return Response({'msg': 'deleted successfully'})
#______________________________________________________________________________________________________________________________________________________________________________________________________-

class productsCartModelLsitCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productsCartModel.objects.all()
    serializer_class = serializers.productsCartModelSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]



    def list(self, request):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.productsCartModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class prodcutsCartUpdateView(APIView):

    def put(self, request, slug, format=None):
        print(request.data)
        cart = productsCartModel.objects.get(slug=slug)
        serializer = serializers.productsCartModelSerializer(data=request.data, instance=cart, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsCartDeleteView(APIView):
    def delete(self, request, slug, format=None):
        cart = productsCartModel.objects.get(slug=slug)
        cart.delete()
        return Response({'msg': 'deleted successfully'})


class productUserCartDetailView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productsCartModel.objects.all()
    serializer_class = serializers.productUserCartDetailSerializer
    pagination_class = LimitOffsetPagination


    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)

class prdocutsingleUserCartGetViews(APIView):

    def get(self, request, slug, *args, **kwargs):
        cart = productsCartModel.objects.filter(slug=slug)
        serializer = serializers.productUsersCartDetailSerializer(cart, many=True)
        return Response(serializer.data)




class productAddProductToCartView(APIView):


    def post(self, request, slug):
        cart = productsCartModel.objects.all()
        query_set = productsAttributeModel.objects.filter(slug=slug)
        if query_set.count() == 1:
            product = query_set.first()
            if product not in cart.products.all():
                cart.products.create(product)
            else:
                cart.products.remove(product)
            request.session[''] = cart.products.count()

        return Response(status=status.HTTP_200_OK, data={'message': 'Product has been added to cart'})

#_______________________________________________________________________________________________________________________________________________________________________________________________________
class productsListOrderModelCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productsOrderModel.objects.all()
    serializer_class = serializers.productsOrderModelSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)

class productsOrderModelLsitCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productsOrderModel.objects.all()
    serializer_class = serializers.productsOrderModelSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)

class productsPlaceOrderModelLsitView(generics.CreateAPIView, generics.ListAPIView):
    queryset = productsCartModel.objects.all()
    serializer_class = serializers.productsUsersOrderSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]


    def post(self, request, slug,*args, **kwargs):
        cart = productsCartModel.objects.get(slug=slug)
        serializer = serializers.productsUsersOrderSerializer(cart,data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class prdocutOrderGetViews(APIView):

    def get(self, request, slug, *args, **kwargs):
        order = productsOrderModel.objects.filter(slug=slug)
        serializer = serializers.productsOrderModelSerializer(order, many=True)
        return Response(serializer.data)


class productsorderDeleteView(APIView):
    def delete(self, request, slug, format=None):
        order = productsOrderModel.objects.get(slug=slug)
        order.delete()
        return Response({'msg': 'deleted successfully'})

class productsUsersOrderModelLsitView(generics.CreateAPIView,generics.ListAPIView):
    queryset = productsOrderModel.objects.all()
    serializer_class = serializers.productsOrderModelSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)


# class productsPaymentOrderModelLsitView(APIView):
#     queryset = productsBrandModel.objects.all()
#     serializer_class = serializers.paymentserailzer
#     pagination_class = LimitOffsetPagination
#
#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(self.paginate_queryset(queryset),
#                                            context={'request': request}, many=True)
#         return self.get_paginated_response(serializer.data)
#
#     def post(self, request,pk, *args, **kwargs):
#
#         order = productsOrderModel.objects.filter(pk=pk)
#         serializer=serializers.paymentserailzer(order,many=True)
#         if serializer.is_valid():
#
#             payment = serializers.productsOrderModelSerializer(data=request.data)
#             if payment.is_valid():
#                 payment.save()
#             serializer.save()
#             return Response({'data': serializer.data})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class prdocutsingleUserOrderGetViews(APIView):

    def get(self, request, slug, *args, **kwargs):
        order = productsOrderModel.objects.filter(slug=slug)
        serializer = serializers.productsOrderModelSerializer(order, many=True)
        return Response(serializer.data)