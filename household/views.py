from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateDestroyOnlyViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        GenericViewSet):
    pass


class UpdateDestroyOnlyViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        GenericViewSet):
    pass
