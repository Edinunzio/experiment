from rest_framework import serializers

from cats.models import Cat, Pair


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ["name", "style", "dob"]


class PairSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pair
        fields = ["cats"]
