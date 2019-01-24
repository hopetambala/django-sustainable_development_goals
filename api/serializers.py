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

class CountryTargetIndicatorSerializer(serializers.ModelSerializer):

    indicator_id = serializers.ReadOnlyField(source='indicator.indicator_id')
    country_area_id = serializers.ReadOnlyField(source='country_area.country_area_id')

    class Meta:
	    model = CountryTargetIndicator
	    fields = ('indicator_id', 'country_area_id')

class IndicatorSerializer(serializers.ModelSerializer):
    target = serializers.PrimaryKeyRelatedField(
		allow_null=False,
		many=False,
		write_only=True,
		queryset=Target.objects.all(),
		#source='target'
	)
    indicator_value_type = serializers.PrimaryKeyRelatedField(
		allow_null=False,
		many=False,
		write_only=True,
		queryset=IndicatorValueType.objects.all(),
		#source='indicator_value_type'
	)
    country_target_indicator = CountryTargetIndicatorSerializer(
		source='country_target_indicator_set', # Note use of _set
		many=True,
		read_only=True
	)
	
    class Meta:
        model = Indicator
        fields = ('indicator_id', 'target','indicator_value_type','country_target_indicator')
    
    def create(self, validated_data):
        """
        This method persists a new Indicator instance as well as adds all related
        countries/areas to the Country Target Indicator table.  It does so by first
        removing (validated_data.pop('heritage_site_jurisdiction')) from the validated
        data before the new HeritageSite instance is saved to the database. It then loops
        over the heritage_site_jurisdiction array in order to extract each country_area_id
        element and add entries to junction/associative heritage_site_jurisdiction table.
        :param validated_data:
        :return: site
        """

        # print(validated_data)

        countries = validated_data.pop('country_target_indicator')
        indicator = Indicator.objects.create(**validated_data)

        if countries is not None:
            for country in countries:
                CountryTargetIndicator.objects.create(
                    indicator_id=indicator.indicator_id,
                    country_area_id=country.country_area_id
                )
        return indicator
    
    def update(self, instance, validated_data):
        # site_id = validated_data.pop('heritage_site_id')
        indicator_id = instance.indicator_id
        new_countries = validated_data.pop('country_target_indicator')

        instance.target = validated_data.get(
            'target',
            instance.target
        )
        instance.indicator_value_type = validated_data.get(
            'indicator_value_type',
            instance.indicator_value_type
        )
        
        instance.save()

        # If any existing country/areas are not in updated list, delete them
        new_ids = []
        old_ids = CountryTargetIndicator.objects \
            .values_list('country_area_id', flat=True) \
            .filter(indicator_id__exact=indicator_id)

        # TODO Insert may not be required (Just return instance)

        # Insert new unmatched country entries
        for country in new_countries:
            new_id = country.country_area_id
            new_ids.append(new_id)
            if new_id in old_ids:
                continue
            else:
                CountryTargetIndicator.objects \
                    .create(indicator_id=indicator_id, country_area_id=new_id)

        # Delete old unmatched country entries
        for old_id in old_ids:
            if old_id in new_ids:
                continue
            else:
                CountryTargetIndicator.objects \
                    .filter(indicator_id=indicator_id, country_area_id=old_id) \
                    .delete()

        return instance

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

