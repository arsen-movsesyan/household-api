# from rest_framework.response import Response
# from rest_framework import status
from passman import serializers, models
from rest_framework.viewsets import ModelViewSet


class PersonViewSet(ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class AddressViewSet(ModelViewSet):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()


class VehicleViewSet(ModelViewSet):
    serializer_class = serializers.VehicleSerializer
    queryset = models.Vehicle.objects.all()


class PersonDocumentViewSet(ModelViewSet):
    serializer_class = serializers.PersonDocumentSerializer
    queryset = models.PersonDocument.objects.all()


class AccountViewSet(ModelViewSet):
    serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()


class RecurringAccountViewSet(ModelViewSet):
    serializer_class = serializers.RecurringAccountSerializer
    queryset = models.RecurringAccount.objects.all()


class RecurringAcknowledgementViewSet(ModelViewSet):
    serializer_class = serializers.RecurringAcknowledgementSerializer
    queryset = models.RecurringAcknowledgement.objects.all()
