from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import random, datetime

@login_required
def index(request):
    now = datetime.datetime.utcnow()
    incidents = [
        {'id':'INC-0831','title':'Suspicious Package','location':'Central Station · Platform 3','cam':'CAM-0083','time':'14:32 UTC','sev':'HIGH','color':'#ff0040'},
        {'id':'INC-0830','title':'Crowd Surge Alert','location':'Market District · Gate 7','cam':'CAM-0247','time':'14:18 UTC','sev':'MED','color':'#ff6b35'},
        {'id':'INC-0829','title':'Vehicle Break-In','location':'Parking Zone B · Level 2','cam':'CAM-0512','time':'13:55 UTC','sev':'MED','color':'#ff6b35'},
        {'id':'INC-0828','title':'Graffiti Detected','location':'Downtown Wall · Main St','cam':'CAM-0112','time':'13:30 UTC','sev':'LOW','color':'#00ff88'},
        {'id':'INC-0827','title':'Traffic Obstruction','location':'Highway 4 · Junction 9','cam':'CAM-0389','time':'12:58 UTC','sev':'LOW','color':'#00ff88'},
    ]
    alerts = [
        {'time':'14:34:12 UTC','text':'🔴 Weapon detected — Zone 3A · CAM-0571'},
        {'time':'14:30:45 UTC','text':'🟠 Crowd density critical — Market Gate 7'},
        {'time':'14:28:02 UTC','text':'🟡 Unattended bag — Central Station P3'},
        {'time':'14:22:18 UTC','text':'🔴 Face match: Watchlist ID #4421'},
        {'time':'14:18:55 UTC','text':'🟢 Patrol unit Alpha reached checkpoint'},
        {'time':'14:15:33 UTC','text':'🟠 Speeding vehicle — Zone 5 · CAM-0088'},
    ]
    ctx = {
        'cameras_online': 1247,
        'active_alerts': 12,
        'incidents_today': 38,
        'officers_on_duty': 94,
        'incidents': incidents,
        'alerts': alerts,
        'now': now.strftime('%H:%M:%S UTC'),
    }
    return render(request, 'dashboard/index.html', ctx)
