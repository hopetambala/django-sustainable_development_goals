# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse



class CountryArea(models.Model):
    country_area_id = models.AutoField(primary_key=True)
    country_area_name = models.CharField(unique=True, max_length=100)
    m49_code = models.SmallIntegerField()
    iso_alpha3_code = models.CharField(max_length=3)
    location = models.ForeignKey('Location', models.DO_NOTHING)
    dev_status = models.ForeignKey('DevStatus', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_area'
        ordering = ['country_area_name']
        verbose_name = 'UNSD M49 Country or Area'
        verbose_name_plural = 'UNSD M49 Countries or Areas'

    def __str__(self):
        return self.country_area_name


class CountryTargetIndicator(models.Model):
    country_target_indicator_id = models.IntegerField(primary_key=True)
    countrycode = models.CharField(max_length=255, blank=True, null=True)
    country_area = models.ForeignKey(CountryArea, models.DO_NOTHING, blank=True, null=True)
    seriescode = models.CharField(max_length=255, blank=True, null=True)
    indicator = models.ForeignKey('Indicator', models.DO_NOTHING, blank=True, null=True)
    indicator_value = models.CharField(db_column='Indicator_Value', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'country_target_indicator'
        ordering = ['indicator_value']
        verbose_name = 'UNMDG Country Indicator'
        verbose_name_plural = 'UNMDG Country Target Indicators'

    def __str__(self):
        return self.indicator_value
    
    def get_absolute_url(self):
        #return reverse('country_target_indicator_detail', args=[str(self.id)])
        return reverse('country_target_indicator_detail', kwargs={'pk': self.pk})


class DevStatus(models.Model):
    dev_status_id = models.AutoField(primary_key=True)
    dev_status_name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'dev_status'
        ordering = ['dev_status_name']
        verbose_name = 'UNSD M49 Country or Area Development Status'
        verbose_name_plural = 'UNSD M49 Country or Area Development Statuses'

    def __str__(self):
        return self.dev_status_name


class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    goal_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goal'
        ordering = ['goal_name']
        verbose_name = 'UNMDG Goal'
        verbose_name_plural = 'UNMDG Goals'

    def __str__(self):
        return self.goal_name


class Indicator(models.Model):
    indicator_id = models.AutoField(primary_key=True)
    target = models.ForeignKey('Target', models.DO_NOTHING)
    indicator_value_type = models.ForeignKey('IndicatorValueType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'indicator'
        

class IndicatorValueType(models.Model):
    indicator_value_type_id = models.AutoField(primary_key=True)
    indicator_value_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicator_value_type'
        ordering = ['indicator_value_name']
        verbose_name = 'UNMDG Indicator Value Name'
        verbose_name_plural = 'UNMDG Indicator Value Names'

    def __str__(self):
        return self.indicator_value_name


class IntermediateRegion(models.Model):
    intermediate_region_id = models.AutoField(primary_key=True)
    intermediate_region_name = models.CharField(unique=True, max_length=100)
    sub_region = models.ForeignKey('SubRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intermediate_region'
        ordering = ['intermediate_region_name']
        verbose_name = 'UNSD M49 Intermediate Region'
        verbose_name_plural = 'UNSD M49 Intermediate Regions'

    def __str__(self):
        return self.intermediate_region_name


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    planet = models.ForeignKey('Planet', models.DO_NOTHING)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True)
    sub_region = models.ForeignKey('SubRegion', models.DO_NOTHING, blank=True, null=True)
    intermediate_region = models.ForeignKey(IntermediateRegion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Planet(models.Model):
    planet_id = models.AutoField(primary_key=True)
    planet_name = models.CharField(unique=True, max_length=50)
    unsd_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planet'
        ordering = ['planet_name']
        verbose_name = 'UNSD Planet Name'
        verbose_name_plural = 'UNSD Planet Names'

    def __str__(self):
        return self.planet_name


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(unique=True, max_length=100)
    planet = models.ForeignKey(Planet, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region'
        ordering = ['region_name']
        verbose_name = 'UNSD M49 Region'
        verbose_name_plural = 'UNSD M49 Regions'

    def __str__(self):
        return self.region_name


class SubRegion(models.Model):
    sub_region_id = models.AutoField(primary_key=True)
    sub_region_name = models.CharField(unique=True, max_length=100)
    region = models.ForeignKey(Region, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_region'
        ordering = ['sub_region_name']
        verbose_name = 'UNSD M49 Subregion'
        verbose_name_plural = 'UNSD M49 Subregions'

    def __str__(self):
        return self.sub_region_name


class Target(models.Model):
    target_id = models.AutoField(primary_key=True)
    target_name = models.CharField(unique=True, max_length=255)
    goal = models.ForeignKey(Goal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'target'
        ordering = ['target_name']
        verbose_name = 'UNMDG Target'
        verbose_name_plural = 'UNMDG Targets'

    def __str__(self):
        return self.target_name
