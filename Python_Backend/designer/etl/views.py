from django.shortcuts import render
import os,sys,inspect
# sys.path.append()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from django.http import HttpResponse, JsonResponse
import Core.Main_excel_parser as MainLoader
from rest_framework import serializers
import json


# Create your views here.

def get_info(request, name, mode):
    try:
        dict_config = MainLoader.MainLoader.api_config(name, opts=mode)
    except:
        return HttpResponse(request)
    return JsonResponse(dict_config)


def get_list_configs(request):
    data = os.listdir(os.path.join(os.getcwd(),'config'))
    return JsonResponse({'list':data})
