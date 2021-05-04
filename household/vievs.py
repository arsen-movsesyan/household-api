from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateDestroyOnlyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    pass
