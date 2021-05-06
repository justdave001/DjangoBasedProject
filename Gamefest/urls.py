
from django.conf.urls import url, include
from django.contrib import admin
from games.views import TemplateView

from django.contrib.auth.views import LoginView, LogoutView
from Gamelists1.views import HomeView
from games.views import gamesCreateView

from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].+)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^u/', include('profiles.urls', namespace='profile')),
    url(r'^items/', include('Gamelists1.urls', namespace='Gamelists1')),
    url(r'^games/', include('games.urls', namespace='games')),

    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact')
]
