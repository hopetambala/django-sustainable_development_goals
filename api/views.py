from unsdg.models import CountryTargetIndicator
from api.serializers import CountryTargetIndicatorSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class CTIndicatorViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = CountryTargetIndicator.objects.select_related('indicator')
	serializer_class = CountryTargetIndicatorSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		cti = self.get_object(pk)
		self.perform_destroy(self, cti)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()