from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from passman import serializers, models
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from household.views import UpdateDestroyOnlyViewSet


class PersonViewSet(ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()

    def destroy(self, request, *args, **kwargs):
        person = self.get_object()
        person.retired = True
        person.save()


class AddressViewSet(UpdateDestroyOnlyViewSet):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()


class AddressCreateView(APIView):

    def post(self, request, **kwargs):
        serializer = serializers.AddressCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address_data = serializer.validated_data
        obj = serializer.create(address_data)
        ret_serializer = serializers.AddressSerializer(obj)
        return Response(ret_serializer.data, status=status.HTTP_201_CREATED)


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


@api_view(http_method_names=['GET'])
def get_constants(request):
    obj = {
        'extras': models.recurring_extras,
        'frequencies': models.frequency_choices
    }
    return Response(obj, status=status.HTTP_200_OK)
