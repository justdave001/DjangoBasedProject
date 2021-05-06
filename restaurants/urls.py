from django.conf.urls import url




from .views import (
    GamesListView,
    GamesDetailView,
    gamesCreateView,
    gameUpdateView
 )



urlpatterns = [
    url(r'^create/$', gamesCreateView.as_view(), name='create'),
    #url(r'^(?P<slug>[\w-]+)/$', GamesDetailView.as_view(), name='detail'),
    #url(r'^email-form/$', gamesCreateView.as_view(), name='email-us'),
    url(r'^(?P<slug>[\w-]+)/$', gameUpdateView.as_view(), name='detail'),
    url(r'$', GamesListView.as_view(), name='list')
]
