from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):
    def get(self, request, borough, activity):
        return render(
            request=request,
            template_name='activities.html',
            context={'borough': borough, 'activity': activity, 'venues' :boroughs[borough][activity].keys()}
        )
    pass


class VenueView(View):
    def get(self, request, borough, activity, venue):
        return render(
            request=request,
            template_name='venues.html',
            context={'borough': borough, 'activity': activity,
            'venue' : venue
            [borough][activity][venue].keys()}
        )
    pass