from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from base.models import Parts
from base.serializers import PartsSerializer, PartDetailSerializer
import time
    
@api_view(['GET','PUT'])
def part_lists(request):

    parts = Parts.objects.all().order_by('-price')
    if 'type' in request.query_params:
        params_dic = request.query_params
        parts = Parts.objects.filter(type=params_dic['type']).order_by('-price')
        if parts.count()==0:
            parts = parts = Parts.objects.all().order_by('-price')
    elif len(request.query_params)>0:
        parts = Parts.objects.all().order_by('-price')
        return Response({'status':1},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = PartsSerializer(parts, many = True)
        avg = round(parts.aggregate(Avg('price'))['price__avg'],2)
        return Response({'status' : 0,
                        'total' : parts.count(),
                        'average_price' : avg,
                        'parts' : serializer.data})
    
    elif request.method == 'PUT':
        serializer = PartDetailSerializer(data = request.data)
        request.data['release_date'] = int(time.time())
        if serializer.is_valid():
            serializer.save()
            return Response({'status':0, 'message':"New part added", 'id': serializer.data['id']}, status= status.HTTP_200_OK)
        else:
            return Response({'status':1, 'message':"Invalid type. Valid choices are 'CPU' and 'GPU'."},
                            status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','POST','PATCH'])
def part_detail(request, ID):
    part = Parts.objects.filter(id = ID)
    if len(part) == 0:
        return Response({'status': 1, 'message':"Part not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PartDetailSerializer(part, many = True)
        return Response({'status': 0 ,'part': serializer.data},status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        part.delete()
        return Response({'status':0, 'message': "Part deleted"},status= status.HTTP_200_OK)
    elif request.method == 'POST':
        obj = Parts.objects.get(id = ID)
        serializer = PartDetailSerializer(data = request.data, instance=obj)
        request.data['release_date'] = int(time.time())
        if serializer.is_valid():
            serializer.save()
            return Response({'status':0, 'message':"Part details updated"}, status= status.HTTP_200_OK)
        else:
            return Response({'status':1}, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        obj = Parts.objects.get(id = ID)
        serializer = PartDetailSerializer(data = request.data, instance= obj,partial = True)
        request.data['release_date'] = int(time.time())
        if serializer.is_valid():
            serializer.save()
            return Response({'status':0, 'message':"Part modified"}, status= status.HTTP_200_OK)
        else:
            return Response({'status':1}, status= status.HTTP_400_BAD_REQUEST)