from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
#from django_filters.views import FilterView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .models import CountryTargetIndicator, CountryArea, Goal, Target,IndicatorValueType
#from .forms import HeritageSiteForm
#from .filters import HeritageSiteFilter


def index(request):
   return HttpResponse("Hello, world. You're at the UNESCO Heritage Sites index.")

class AboutPageView(generic.TemplateView):
	template_name = 'unsdg/about.html'

class HomePageView(generic.TemplateView):
	template_name = 'unsdg/home.html'


class GoalListView(generic.ListView):
    model = Goal
    context_object_name = 'goals'
    template_name = 'unsdg/goal.html'
    paginate_by = 50

    def get_queryset(self):
        #return HeritageSite.objects.all().select_related('heritage_site_category').order_by('site_name')
        return Goal.objects.all()

class CountryListView(generic.ListView):
	model = CountryArea	
	context_object_name = 'countries'
	template_name = 'heritagesites/country_area.html'
	paginate_by = 20

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return CountryArea.objects.all().select_related('dev_status').order_by('country_area_name')

class IndicatorListView(generic.ListView):
	model = IndicatorValueType
	context_object_name = 'indicator_names'
	template_name = 'unsdg/indicator_names.html'
	paginate_by = 50

	def get_queryset(self):
		return IndicatorValueType.objects.all() 