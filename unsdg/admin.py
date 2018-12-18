from django.contrib import admin

import unsdg.models as models


admin.register(models.CountryArea)

admin.register(models.DevStatus)

admin.register(models.IntermediateRegion)

admin.register(models.Region)

admin.register(models.SubRegion)

admin.register(models.Planet)

admin.register(models.Location)

admin.register(models.Goal)

admin.register(models.Indicator)

admin.register(models.IndicatorValueType)

admin.register(models.CountryTargetIndicator)