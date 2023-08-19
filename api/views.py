from django.shortcuts import render
from django.views import generic
from rest_framework import generics, status
from .models import NameList
from .serializers import NameListSerializer
from rest_framework.response import Response

# Create your views here.
class NameListView(generics.GenericAPIView):
    serializer_class = NameListSerializer

    def get(self, request):
        name_data = []
        name_list = NameList.objects.all()
        for name_object in name_list:
            name_data.append(
                {'name': name_object.name, 'age': name_object.age, 'phone': name_object.phone, 'email': name_object.email}
            )
        return Response(data=name_data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": "success", "message": "Person added to Name List"}
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        response = {"status": "fail", "message": serializer.errors}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        try:
            person = NameList.objects.get(email=request.GET.get('email'))
        except:
            person = None

        if person != None:
            serializer = self.serializer_class(instance=person, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response = {"status": "success", "message": "Person details has been updated"}
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                response = {"status": "fail", "message": serializer.errors}
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        
        response = {"status": "fail", "message": f"Person with email '{request.GET.get('email')}' not found"}
        return Response(data=response, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request):
        try:
            person = NameList.objects.get(email=request.data.get('email'))
        except:
            person = None

        if person != None:
            person.delete()
            response = {"status": "success", "message": "Person deleted from Name List"}
            return Response(data=response, status=status.HTTP_204_NO_CONTENT)
        
        response = {"status": "fail", "message": f"Person with email '{request.data.get('email')}' not found"}
        return Response(data=response, status=status.HTTP_404_NOT_FOUND)