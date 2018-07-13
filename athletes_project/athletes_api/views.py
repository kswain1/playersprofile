from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializer

# Create your views here.

class HelloApiView(APIView):
	""" Test API View"""

	serializers_class = serializer.HelloSerializer


	def get(self, request, format=None):
		""" Returns a list of API Function Methods"""

		an_apiview = [
			"Uses Http methods as function (get,post, patch,put,delete",
			"It is similar to a traditional Django view",
			"Give you the most control over your logic",
			"Is mapped manually to URLS"

		]

		return Response({'message': 'Hello!', "an_apiview":an_apiview})

	def post(self, request):
		"""Create a hello message with our name"""

		serial = serializer.HelloSerializer(data=request.data)

		if serial.is_valid():
			name = serial.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message':message})
		else: 
			return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		"""HAndles updating string object"""

		return Response({'method': 'put'})

	def patch(self,request, pk=None):
		"""Patch request, only updates fields provided in the request"""

		return Response({'method':'patch'})

	def delete(self, request, pk=None):
		"""Deletes and object"""

		return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet"""

	def list(self, request):
		""" return a hello message"""


		a_viewset = [
			'uses acitons (list, create, retrieve, update, partial_update',
			'Automatically maps to URLs using Routers',
			'Provides more functionally with less code'
			]

		return Response({'message':'Hello!','a_viewset':a_viewset})

