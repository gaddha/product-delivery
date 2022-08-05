from django.shortcuts import render
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . models import User
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

class accountProfileListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.accountUserListserializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(self.paginate_queryset(queryset),
                                           context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)


class accountsUserCreationView(generics.GenericAPIView):
    serializer_class = serializers.accountsUserCreationSerializer

    def post(self,request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UpdateUserSerializer


    # def put(self, request, slug, format=None):
    #     print(request.data)
    #     user = User.objects.get(slug=slug)
    #     serializer = serializers.UpdateUserSerializer(data=request.data, instance=user, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': serializer.data})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

