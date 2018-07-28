from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from . import serializer
from . import models
from . import permissions

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

	serializer_class = serializer.HelloSerializer

	def list(self, request):
		""" return a hello message"""

		a_viewset = [
			'uses acitons (list, create, retrieve, update, partial_update',
			'Automatically maps to URLs using Routers',
			'Provides more functionally with less code'
			]

		return Response({'message':'Hello!','a_viewset':a_viewset})

	def create(self, request): 
		""" Create a new hello message """

		serial = serializer.HelloSerializer(data=request.data)

		if serial.is_valid():
			name = serial.data.get('name')
			message = "Hello {0}".format(name)
			return Response({'message':message})

		else: 
			return Response(
				serial.errors, status=status.HTTP_400_BAD_REQUEST
				)

	def retrieve(self, request, pk=None):
		"""handles getting an object by its ID."""

		return Response({'http_method': 'GET'})


	def update(self, request, pk=None):
		"""handles updating an object"""

		return Response({'http_method': 'PUT'})


	def partial_update(self,request, pk=None):
		"""handles updating part of an object"""

		return Response({'http_method': 'PATCH'})


	def destroy(self, request, pk=None):
		"""handles removing objects"""

		return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
	"""handles creating, creating and updating profiles"""

	serializer_class = serializer.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)







