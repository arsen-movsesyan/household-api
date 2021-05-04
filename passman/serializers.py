from rest_framework import serializers
from passman import models


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    # address_line1 = serializers.CharField(required=False)
    # city = serializers.CharField(required=False)
    # state = serializers.CharField(required=False)
    # zip_code = serializers.CharField(required=False)

    class Meta:
        model = models.Address
        fields = '__all__'


class AddressCreateSerializer(serializers.Serializer):
    address_line1 = serializers.CharField()
    address_line2 = serializers.CharField(allow_null=True, required=False)
    apt_suite = serializers.CharField(allow_null=True, required=False)
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
    period_start = serializers.DateField()
    period_end = serializers.DateField(allow_null=True)
    comment = serializers.CharField(allow_null=True, required=False)

    def create(self, validated_data):
        return models.Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vehicle
        fields = '__all__'


class PersonDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PersonDocument
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = '__all__'


class RecurringAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RecurringAccount
        fields = '__all__'


class RecurringAcknowledgementSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RecurringAcknowledgement
        fields = '__all__'
