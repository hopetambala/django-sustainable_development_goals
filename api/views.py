from unsdg.models import Indicator
from api.serializers import IndicatorSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class IndicatorViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	#queryset = HeritageSite.objects.select_related('heritage_site_category').order_by('site_name')
	queryset = Indicator.objects.select_related('target')
	serializer_class = IndicatorSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		site = self.get_object(pk)
		self.perform_destroy(self, site)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()