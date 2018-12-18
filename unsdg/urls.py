from django.urls import path

from . import views

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('cti/', views.CountryTargetIndicatorListView.as_view(), name='country_target_indicators'),
   path('cti/<int:pk>', views.CountryTargetIndicatorDetailView.as_view(), name='country_target_indicator_detail'),
   path('about/', views.AboutPageView.as_view(), name='about'),
   path('indicator_value_names/', views.IndicatorNameListView.as_view(), name='indicator_names'),
   path('goals/', views.GoalListView.as_view(), name='goals'),
   path('targets/', views.TargetListView.as_view(), name='targets'),
]