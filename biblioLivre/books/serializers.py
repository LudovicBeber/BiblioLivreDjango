from rest_framework import serializers
from .models import Livre, Avis

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ['id', 'name', 'author', 'year']

class AvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = ['id', 'commentaire', 'rating', 'user', 'livre']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La note doit être comprise entre 1 et 5.")
        return value
