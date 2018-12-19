from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import path, include


urlpatterns = [
    path('', lambda r: HttpResponseRedirect('unsdg/')),
    path('admin/', admin.site.urls),
    path('unsdg/', include('unsdg.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('api-auth/', include('rest_framework.urls')),
    path('unsdg/api/', include('api.urls')),
    path('unsdg/api/rest-auth/', include('rest_auth.urls')),
    path('unsdg/api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]