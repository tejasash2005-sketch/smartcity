from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    hotspots = [
        {'name':'Zone 3 · Airport','lat':12.9941,'lng':77.6685,'sev':'HIGH','incidents':11},
        {'name':'Zone 5 · Market','lat':12.9716,'lng':77.5946,'sev':'HIGH','incidents':9},
        {'name':'Zone 1 · Downtown','lat':12.9784,'lng':77.6408,'sev':'MED','incidents':8},
        {'name':'Zone 2 · Harbor','lat':13.0067,'lng':77.5975,'sev':'LOW','incidents':4},
        {'name':'Zone 4 · Central Park','lat':12.9850,'lng':77.6100,'sev':'LOW','incidents':3},
    ]
    patrols = [
        {'id':'P-01','officer':'Sgt. Priya Shah','zone':'Zone 5','status':'ACTIVE'},
        {'id':'P-02','officer':'Cpl. Ravi Mehta','zone':'Zone 3','status':'ACTIVE'},
        {'id':'P-03','officer':'Const. Arjun Nair','zone':'Zone 1','status':'BREAK'},
    ]
    return render(request, 'map/index.html', {'hotspots': hotspots, 'patrols': patrols})
