from django.conf.urls.defaults import *

urlpatterns = patterns('uplayn.groupadmin.views',
    (r'^set-game-times/$', 'set_game_times'),
)
