from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *



class SavolAPIView(ModelViewSet):
    serializer_class = SavolSerializer
    queryset = Savol.objects.all()
    def get(self, request):
        search = request.query_params.get('search')
        print(search)
        savollar = Savol.objects.all()
        if search is not None:
            print('kirdi')
            savollar = savollar.filter(sarlavha__icontains=search)
        serializer = SavolSerializer(savollar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SavolarAPIView(APIView):
    # pagination_class =
    def get(self, request):
        soz = request.query_params.get('search')
        if soz:
            natija = Savol.objects.filter(texnologiya__contains=soz)
        else:
            natija = Savol.objects.all()
        serializer = SavolSerializer(natija.order_by('-sana'), many=True)
        return Response(serializer.data)

# class SavollarViews(generics.ListAPIView, generics.CreateAPIView):
#     quaryset = Savol.objects.all()
    # serializer_class = SavolSerializer

class SavolViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Savol.objects.all()
    serializer_class = SavolSerializer

class SavollarViews(generics.ListCreateAPIView):
    queryset = Savol.objects.all()
    serializer_class = SavolSerializer

class Savol_JavoblariAPIView(APIView):
    def get(self, request, pk):
        natija = Javob.objects.filter(savol__id=pk)
        serializer = JavobSerializer(natija, many=True)
        return Response(serializer.data)

class SavolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Savol.objects.all()
    serializer_class = SavolSerializer

class ReaksiyaPOSTAPIView(APIView):
    def get(self, request):
        natija = Reaksiya.objects.all()
        serializer = ReaksiyaSerializer(natija, many=True)
        return Response(serializer.data)


    def post(self, request):
        # reaksiya = ReaksiyaSerializer(request.data, many=True)
        reaksiya = request.data
        if reaksiya['User'] == request.user.id:
            Izoh.objects.get(javob__id=reaksiya['javob']).update(baho=reaksiya['baho'])

            return Response({'success': True})
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)