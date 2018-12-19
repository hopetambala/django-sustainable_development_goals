import django_filters
from .models import CountryArea, Region,IndicatorValueType ,Indicator, Target, Goal, CountryTargetIndicator


class CountryTargetIndicatorFilter(django_filters.FilterSet):
    goal = django_filters.ModelChoiceFilter(
        field_name='indicator__target__goal__goal_name',
        label='Goal',
        queryset=Goal.objects.all().order_by('goal_name'),
        lookup_expr='icontains'
    )

    target = django_filters.ModelChoiceFilter(
        field_name='indicator__target__target_name',
        label='Target',
        queryset=Target.objects.all().order_by('target_name'),
        lookup_expr='icontains'
    )

    indicator = django_filters.ModelChoiceFilter(
        field_name='indicator__indicator_value_type__indicator_value_name',
        label='Indicator',
        queryset=IndicatorValueType.objects.all(),
        lookup_expr='icontains'
    )


    indicator_value = django_filters.CharFilter(
        field_name='indicator_value',
        label='Indicator Value',
        lookup_expr='icontains'
    )

    #Fix
    region = django_filters.ModelChoiceFilter(
        field_name='country_area__location__region__region_name',
        label='Region',
        queryset=Region.objects.all().order_by('region_name'),
        lookup_expr='exact'
    )
    '''
    sub_region = django_filters.ModelChoiceFilter(
        field_name='country_area__location__sub_region__sub_region_name',
        label='SubRegion',
        queryset=SubRegion.objects.all().order_by('sub_region_name'),
        lookup_expr='exact'
    )

    intermediate_region = django_filters.ModelChoiceFilter(
        field_name='country_area__location__intermediate_region__intermediate_region_name',
        label='Intermediate Region',
        queryset=IntermediateRegion.objects.all().order_by('intermediate_region_name'),
        lookup_expr='exact'
    )
    '''
    
    country_area = django_filters.ModelChoiceFilter(
        field_name='country_area',
        label='Country/Area',
        queryset=CountryArea.objects.all().order_by('country_area_name'),
        lookup_expr='exact'
    )

    year = django_filters.NumberFilter(
		field_name='year',
		label='Year',
		lookup_expr='exact'
	)


    class Meta:
        model = CountryTargetIndicator
        # form = SearchForm
        # fields [] is required, even if empty.
        fields = []