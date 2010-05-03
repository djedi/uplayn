from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required

@login_required
def set_game_times(request):
    return direct_to_template(request, 'groupadmin/set_game_times.html', {})
