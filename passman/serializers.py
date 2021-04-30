from rest_framework.serializers import ModelSerializer
from passman import models


class PersonSerializer(ModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'


class AddressSerializer(ModelSerializer):

    class Meta:
        model = models.Address
        fields = '__all__'


class VehicleSerializer(ModelSerializer):

    class Meta:
        model = models.Vehicle
        fields = '__all__'


class PersonDocumentSerializer(ModelSerializer):

    class Meta:
        model = models.PersonDocument
        fields = '__all__'


class AccountSerializer(ModelSerializer):

    class Meta:
        model = models.Account
        fields = '__all__'


class RecurringAccountSerializer(ModelSerializer):

    class Meta:
        model = models.RecurringAccount
        fields = '__all__'


class RecurringAcknowledgementSerializer(ModelSerializer):

    class Meta:
        model = models.RecurringAcknowledgement
        fields = '__all__'
