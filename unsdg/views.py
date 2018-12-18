from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django_filters.views import FilterView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .models import CountryTargetIndicator, CountryArea, Goal, Target,IndicatorValueType
from .forms import CountryTargetIndicatorForm
#from .filters import HeritageSiteFilter


def index(request):
   return HttpResponse("Hello, world. You're at the United Nations Sites index.")

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
	paginate_by = 1000

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		#return CountryTargetIndicator.objects.select_related('indicator').values_list('country_area__country_area_name','indicator__target__goal__goal_name','indicator__target__target_name','indicator__indicator_value_type__indicator_value_name','indicator_value')
		return CountryTargetIndicator.objects\
				.select_related('indicator')\
				.values_list('country_area__country_area_name','indicator__target__goal__goal_name','indicator__target__target_name','indicator__indicator_value_type__indicator_value_name','indicator_value','country_target_indicator_id')

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


@method_decorator(login_required, name='dispatch')
class CTIndicatorCreateView(generic.View):
	model = CountryTargetIndicator
	form_class = CountryTargetIndicatorForm
	success_message = "Indicator created successfully"
	template_name = 'unsdg/site_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = CountryTargetIndicatorForm(request.POST)
		if form.is_valid():
			print('Valid Form')
			ctindicator = form.save(commit=False)
			ctindicator.save()
			
			for country in form.cleaned_data['country_area']:
				CountryTargetIndicator.objects.create(country_target_indicator=ctindicator, country_area=country)
			
			return redirect(ctindicator) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		return render(request, 'unsdg/country_target_indicators_new.html', {'form': form})

	def get(self, request):
		form = CountryTargetIndicatorForm()
		return render(request, 'unsdg/country_target_indicators_new.html', {'form': form})

class CTIndicatorUpdateView(generic.UpdateView):
	model = CountryTargetIndicator
	form_class = CountryTargetIndicatorForm
	context_object_name = 'country_target_indicator'
	# pk_url_kwarg = 'site_pk'
	success_message = "Country Target Indicator updated successfully"
	template_name = 'unsdg/country_target_indicators_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		ctindicator = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		ctindicator.save()

		# Current country_area_id values linked to site
		old_ids = CountryTargetIndicator.objects\
			.values_list('country_area_id', flat=True)\
			.filter(country_target_indicator_id=ctindicator.country_target_indicator_id)

		# New countries list
		new_countries = form.cleaned_data['country_area']

		# New ids
		new_ids = []

		# Insert new unmatched country entries
		for country in new_countries:
			new_id = country.country_area_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				CountryTargetIndicator.objects.create(country_target_indicator=ctindicator, country_area=country)

		# Delete old unmatched country entries
		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				CountryTargetIndicator.objects \
					.filter(country_target_indicator_id=ctindicator.country_target_indicator_id, country_area_id=old_id) \
					.delete()

		return HttpResponseRedirect(ctindicator.get_absolute_url())
		# return redirect('heritagesites/site_detail', pk=site.pk)

@method_decorator(login_required, name='dispatch')
class CTIndicatorDeleteView(generic.DeleteView):
	model = CountryTargetIndicator
	success_message = "Country Target Indicator deleted successfully"
	success_url = reverse_lazy('country_target_indicators')
	context_object_name = 'country_target_indicator'
	template_name = 'unsdg/country_target_indicators_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete HeritageSiteJurisdiction entries
		CountryTargetIndicator.objects \
			.filter(country_target_indicator_id=self.object.country_target_indicator_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())