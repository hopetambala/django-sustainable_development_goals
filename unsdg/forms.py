from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from unsdg.models import CountryTargetIndicator, CountryArea,IndicatorValueType

''
class CountryTargetIndicatorForm(forms.ModelForm):

	class Meta:
		model = CountryTargetIndicator
		fields = '__all__'
		#fields = ['country_area, seriescode','countrycode','indicator','indicator_value','year']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#self.fields['indicator'].queryset = IndicatorValueType.objects.filter(user=user)


		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))