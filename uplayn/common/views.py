from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template

from uplayn.groupsites import views as gviews
from uplayn.common.forms import StartGroupForm

def home(request):
    if request.subdomain:
        return gviews.home(request)
    else:
        return direct_to_template(request, 'home.html')

def start_group(request):
    if request.method == 'POST':
        f = StartGroupForm(request.POST)
        if f.is_valid():
            f.save()
            # TODO: send email,
            # send to login prompt to begin creating group page
    else:
        f = StartGroupForm()
    return direct_to_template(request, 'start_group.html', {'form': f})
