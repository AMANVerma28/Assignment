# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Farmerinfo
from .serializers import FarmerinfoSerializer

# Create your views here.
#List all farmer info or create a new one
#farmerinfo/

"""class farmerinfo_list(APIView):
	def get(self, request):
		info = Farmerinfo.objects.all()
		serializer = FarmerinfoSerializer(info, many=True)
		return Response(serializer.data)

	def post(self):
		pass
"""

@csrf_exempt
def farmerinfo_list(request):
#	List all code snippets, or create a new snippet.
	if request.method == 'GET':
		info = Farmerinfo.objects.all()
		serializer = FarmerinfoSerializer(info, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = FarmerinfoSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def farmerinfo_detail(request, pk):
#    Retrieve, update or delete a code snippet.
    try:
        info = Farmerinfo.objects.get(pk=pk)
    except Farmerinfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FarmerinfoSerializer(info)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FarmerinfoSerializer(info, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        info.delete()
        return HttpResponse(status=204)