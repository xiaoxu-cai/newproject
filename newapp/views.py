from django.shortcuts import render

# Create your views here.
import json
import datetime
import time
import uuid
from xpinyin import Pinyin
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



class AddInfo(APIView):
    def post(self, request):
        print(request.data)
        return Response(data={})
