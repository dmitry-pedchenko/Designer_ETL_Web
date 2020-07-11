from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Core import Main_excel_parser as MainLoader
from rest_framework import serializers
import json


# Create your views here.

def get_info(request, name, mode):
    try:
        dict_config = MainLoader.MainLoader.api_config(name, opts=mode)
    except:
        return HttpResponse(request)
    return JsonResponse(dict_config)
