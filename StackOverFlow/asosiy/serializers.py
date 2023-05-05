from django.db.models import Sum
from rest_framework import serializers
from .models import *

# from django.core.validators import MinValueValidator
# from django.db.models import Avg

class SavolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savol
        fields = '__all__'
    def to_representation(self, instance):
        savol = super().to_representation(instance)
        javoblar = Javob.objects.filter(savol=instance)
        serializer = JavobSerializer(javoblar, many=True)
        savol['javoblar'] = serializer.data
        return savol

class JavobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Javob
        fields = '__all__'
    def to_representation(self, instance):
        javob = super().to_representation(instance)
        reaksiyalar = Reaksiya.objects.filter(javob=instance)
        yigindi = reaksiyalar.aggregate(s=Sum('baho')).get('s')
        javob['ovoz_soni'] = yigindi

        izohlar = Izoh.objects.filter(javob=instance)

        javob['izohlar'] = IzohSerializer(izohlar, many=True).data
        return javob

class ReaksiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaksiya
        fields = '__all__'

class NishonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nishon
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'

