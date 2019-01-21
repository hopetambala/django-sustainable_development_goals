from django.urls import path

from . import views

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('cti/', views.CountryTargetIndicatorListView.as_view(), name='country_target_indicators'),
   path('cti/<int:pk>/', views.IndicatorDetailView.as_view(), name='indicator_detail'),
   #path('cti/<int:pk>/', views.CountryTargetIndicatorDetailView.as_view(), name='country_target_indicator_detail'), #possibly bad?
   path('cti/new/', views.IndicatorCreateView.as_view(), name='indicator_new'),
   #path('cti/new/', views.CountryTargetIndicatorCreateView.as_view(), name='country_target_indicator_new'),#possibly bad?
   path('cti/<int:pk>/delete/', views.IndicatorDeleteView.as_view(), name='indicator_delete'),
   path('cti/<int:pk>/update/', views.IndicatorUpdateView.as_view(), name='indicator_update'),
   path('cti/filter/', views.CTIndicatorFilterView.as_view(), name='country_target_indicator_filter'),
   path('about/', views.AboutPageView.as_view(), name='about'),
   path('indicator_value_names/', views.IndicatorNameListView.as_view(), name='indicator_names'),
   path('goals/', views.GoalListView.as_view(), name='goals'),
   path('targets/', views.TargetListView.as_view(), name='targets'),
]