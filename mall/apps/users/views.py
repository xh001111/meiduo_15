from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from users.models import User
# from apps.users.models import User        #错误的

# apps.users 我们已经告知系统 users 在哪里了,就需要添加 apps

"""
一, 确定需求
二,  确定采用哪种请求方式 和 url
三,  实现


1.前端发送一个ajax请求,给后端,参数是 用户名

# 2.后端接收用户名
# 3.查询校验是否重复
# 4.返回响应

GET     /users/usernames/(?P<username>\w{5,20})/count/



"""
# APIView
# GenericAPIView                    列表,详情通用支持,一般和mixin配合使用
# ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
"""
1.前段传递过来的数据 已经在 url中校验过了
2. 我们也不需要 序列化器
"""
class RegisterUsernameCountView(APIView):

    def get(self,request,username):

        count = User.objects.filter(username=username).count()

        return Response({"count":count})

