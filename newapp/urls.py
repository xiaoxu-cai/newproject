#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"
from django.urls import path
from newapp import views

# router = DefaultRouter()
# router.register(prefix="upload", viewset=views.CarouselViewSet)

urlpatterns = [
    path("addinfo", views.AddInfo.as_view(), name="AddInfo"),

]
