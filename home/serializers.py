from rest_framework import serializers

from .models import Order, Food


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('items', 'price')

    def validate(self, data):
        print(data)
        # for item in data.items:
        #     if not Food.objects.filter(name=item.name).exists():
        #         error = "Error, Food Doesn't Exists"
        #         raise serializers.ValidationError(error)

        return data

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order
