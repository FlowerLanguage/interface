from django.shortcuts import render
from foreign_currency.serializers import ForeignCurrencySerializer
from foreign_currency.models import ForeignCurrency
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.versioning import URLPathVersioning
from rest_framework import exceptions


# Create your views here.
class ForeignCurrencyListView(GenericAPIView):
    """
    列表视图类
    包含get,post等方法
    """
    queryset = ForeignCurrency.objects.all()  # 指定哪个模型中的查询集
    serializer_class = ForeignCurrencySerializer  # 指定内部的序列化器
    permission_classes = [AllowAny]  # 指定允许哪些用户可以访问

    filter_backends = [DjangoFilterBackend]  # 指定过滤器
    filterset_fields = ['id', 'symbol']  # 指定哪些字段可以筛选
    versioning_class = URLPathVersioning  # 指定版本控制相关的类

    def get(self, request, *args, **kwargs):  # 返回所有数据
        version = request.version  # 获取前端传来的版本号
        if version == 'v1':
            data = self.get_queryset()  # 获取查询集
            data = self.filter_queryset(data)  # 获取过滤后的数据
            page = self.paginate_queryset(data)  # 获取分页后的数据
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)  # 返回分页的查询结果
            serializer = self.get_serializer(data, many=True)  # 得到一个序列化器的实列
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):  # 新增数据
        data = request.data
        if isinstance(data, dict):  # 如果传过来一个字典，即是一个数据，设置many等于False
            many = False
        elif isinstance(data, list):  # 如果传过来一个列表，即是多个数据，设置many等于True
            many = True
        else:
            raise exceptions.ValidationError('数据格式不正确')
        serializer = self.get_serializer(data=data, many=many)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ForeignCurrencyDetailView(GenericAPIView):
    """
    详情视图类
    包含get,put,delet等三个方法
    """
    queryset = ForeignCurrency.objects.all()  # 指定哪个模型中的查询集
    serializer_class = ForeignCurrencySerializer  # 指定内部的序列化器
    permission_classes = [AllowAny]  # 指定允许哪些用户可以访问

    def get(self, request, pk):  # 找到单个数据
        data = self.get_object()  # 根据传来的pk,找到单个数据
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def put(self, request, pk):  # 根据前端传来的pk修改该条数据
        data = self.get_object()
        serializer = self.get_serializer(data, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):  # 删除找到的单个数据
        data = self.get_object()
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
