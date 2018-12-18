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
    context_object_name = 'goal_list'
    template_name = 'unsdg/goals.html'
    paginate_by = 50

    def get_queryset(self):
        return Goal.objects.all()

class TargetListView(generic.ListView):
    model = Target
    context_object_name = 'target_list'
    template_name = 'unsdg/targets.html'
    paginate_by = 20

    def get_queryset(self):
        return Target.objects.all()

@method_decorator(login_required, name='dispatch')
class CountryTargetIndicatorListView(generic.ListView):
	model = CountryTargetIndicator	
	context_object_name = 'country_target_indicators_list'
	template_name = 'unsdg/country_target_indicators.html'
	paginate_by = 200

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		#return CountryTargetIndicator.objects.select_related('indicator').values_list('country_area__country_area_name','indicator__target__goal__goal_name','indicator__target__target_name','indicator__indicator_value_type__indicator_value_name','indicator_value')
		return CountryTargetIndicator.objects.select_related('indicator').values_list('country_area__country_area_name','indicator__target__goal__goal_name','indicator__target__target_name','indicator__indicator_value_type__indicator_value_name','indicator_value','country_target_indicator_id')

class CountryTargetIndicatorDetailView(generic.DetailView):
	model = CountryTargetIndicator
	context_object_name = 'country_target_indicator_detail'
	template_name = 'unsdg/country_target_indicator_details.html'

	def get_context_data(self, **kwargs):
		context = super(CountryTargetIndicatorDetailView, self).get_context_data(**kwargs)
		context['cti_list'] = CountryTargetIndicator.objects.all().select_related('indicator').filter(country_target_indicator_id=self.kwargs['pk'])
		print(context)
		# And so on for more models
		return context

class IndicatorNameListView(generic.ListView):
	model = IndicatorValueType
	context_object_name = 'indicator_name_list'
	template_name = 'unsdg/indicator_names.html'
	paginate_by = 20

	def get_queryset(self):
		return IndicatorValueType.objects.all()