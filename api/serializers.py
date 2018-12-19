from unsdg.models import CountryArea, DevStatus, CountryTargetIndicator, Indicator,IndicatorValueType, Goal, Target, Location, Planet, Region, SubRegion, IntermediateRegion
from rest_framework import response, serializers, status


class PlanetSerializer(serializers.ModelSerializer):

	class Meta:
		model = Planet
		fields = ('planet_id', 'planet_name', 'unsd_name')

class RegionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Region
		fields = ('region_id', 'region_name', 'planet_id')

class SubRegionSerializer(serializers.ModelSerializer):

	class Meta:
		model = SubRegion
		fields = ('sub_region_id', 'sub_region_name', 'region_id')

class IntermediateRegionSerializer(serializers.ModelSerializer):

	class Meta:
		model = IntermediateRegion
		fields = ('intermediate_region_id', 'intermediate_region_name', 'sub_region_id')

class LocationSerializer(serializers.ModelSerializer):
	planet = PlanetSerializer(many=False, read_only=True)
	region = RegionSerializer(many=False, read_only=True)
	sub_region = SubRegionSerializer(many=False, read_only=True)
	intermediate_region = IntermediateRegionSerializer(many=False, read_only=True)

	class Meta:
		model = Location
		fields = ('location_id', 'planet', 'region', 'sub_region', 'intermediate_region')

class DevStatusSerializer(serializers.ModelSerializer):

	class Meta:
		model = DevStatus
		fields = ('dev_status_id', 'dev_status_name')

class GoalSerializer(serializers.ModelSerializer):

	class Meta:
		model = Goal
		fields = ('goal_id', 'goal_name')

class TargetSerializer(serializers.ModelSerializer):
    goal = GoalSerializer(many=False, read_only=True)

    class Meta:
        model = Target
        fields = ('target_id', 'target_name','goal')

class IndicatorValueTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = IndicatorValueType
		fields = ('indicator_value_type_id', 'indicator_value_name')

class IndicatorSerializer(serializers.ModelSerializer):
    target = TargetSerializer(many=False, read_only=True)
    indicator_value_type = IndicatorValueTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Indicator
        fields = ('indicator_id', 'target','indicator_value_type')

class CountryAreaSerializer(serializers.ModelSerializer):
	dev_status = DevStatusSerializer(many=False, read_only=True)
	location = LocationSerializer(many=False, read_only=True)

	class Meta:
		model = CountryArea
		fields = (
			'country_area_id',
			'country_area_name',
			'm49_code',
			'iso_alpha3_code',
			'dev_status',
			'location')

class CountryTargetIndicatorSerializer(serializers.ModelSerializer):

    year = serializers.IntegerField(
        allow_null=True
    )
    
    country_area = CountryAreaSerializer(
        many=False,
        read_only=True
    )

    indicator = IndicatorSerializer(
		many=False,
		read_only=True
	)
	
    class Meta:
        model = CountryTargetIndicator
        fields = (
            'country_target_indicator_id',
            'country_area',
            'indicator',
            'year',
            'indicator_value'
        )

    def create(self, validated_data):
        """
        This method persists a new HeritageSite instance as well as adds all related
        countries/areas to the heritage_site_jurisdiction table.  It does so by first
        removing (validated_data.pop('heritage_site_jurisdiction')) from the validated
        data before the new HeritageSite instance is saved to the database. It then loops
        over the heritage_site_jurisdiction array in order to extract each country_area_id
        element and add entries to junction/associative heritage_site_jurisdiction table.
        :param validated_data:
        :return: site
        """

        # print(validated_data)

        countries = validated_data.pop('country_area')
        cti = CountryTargetIndicator.objects.create(**validated_data)

        if countries is not None:
            for country in countries:
                CountryTargetIndicator.objects.create(
                    country_target_indicator_id=cti.country_target_indicator_id,
                    country_area_id=country.country_area_id
                )
        return cti

    def update(self, instance, validated_data):
        # site_id = validated_data.pop('heritage_site_id')
        cti_id = instance.country_target_indicator_id
        new_countries = validated_data.pop('country_area')
        
        instance.year = validated_data.get(
            'year',
            instance.year
        )
        
        instance.indicator_id = validated_data.get(
            'indicator_id',
            instance.indicator_id
        )

        instance.indicator_value = validated_data.get(
            'indicator_value',
            instance.indicator_value
        )
        
        instance.save()

        # If any existing country/areas are not in updated list, delete them
        new_ids = []
        old_ids = CountryTargetIndicator.objects \
            .values_list('country_area_id', flat=True) \
            .filter(country_target_indicator_id__exact=cti_id)

        # Insert new unmatched country entries
        for country in new_countries:
            new_id = country.country_area_id
            new_ids.append(new_id)
            if new_id in old_ids:
                continue
            else:
                CountryTargetIndicator.objects \
                    .create(country_target_indicator_id=cti_id, country_area_id=new_id)

        # Delete old unmatched country entries
        for old_id in old_ids:
            if old_id in new_ids:
                continue
            else:
                CountryTargetIndicator.objects \
                    .filter(country_target_indicator_id=cti_id, country_area_id=old_id) \
                    .delete()

        return instance