from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    alerts = [
        {'id':'ALT-0071','time':'14:34:12 UTC','type':'WEAPON','title':'Weapon Detected','desc':'Firearm identified by AI model at Airport Terminal B','cam':'CAM-0383','zone':'Zone 3A','sev':'CRITICAL','color':'#ff0040','status':'ACTIVE'},
        {'id':'ALT-0070','time':'14:30:45 UTC','type':'CROWD','title':'Critical Crowd Density','desc':'Overcrowding threshold exceeded at Market Gate 7','cam':'CAM-0565','zone':'Zone 5','sev':'HIGH','color':'#ff0040','status':'ACTIVE'},
        {'id':'ALT-0069','time':'14:28:02 UTC','type':'OBJECT','title':'Unattended Object','desc':'Suspicious bag left unattended >10 min at platform','cam':'CAM-0083','zone':'Central Stn','sev':'HIGH','color':'#ff0040','status':'INVESTIGATING'},
        {'id':'ALT-0068','time':'14:22:18 UTC','type':'FACE','title':'Watchlist Match','desc':'Face recognition match: Subject ID #4421 detected','cam':'CAM-0247','zone':'Zone 2','sev':'HIGH','color':'#ff6b35','status':'ACTIVE'},
        {'id':'ALT-0067','time':'14:18:55 UTC','type':'VEHICLE','title':'Speeding Vehicle','desc':'Vehicle exceeded 80km/h in 40km/h zone','cam':'CAM-0088','zone':'Zone 5','sev':'MED','color':'#ff6b35','status':'RESOLVED'},
        {'id':'ALT-0066','time':'14:15:33 UTC','type':'INTRUSION','title':'Perimeter Breach','desc':'Motion detected in restricted area after hours','cam':'CAM-0691','zone':'Zone 6','sev':'MED','color':'#ff6b35','status':'RESOLVED'},
        {'id':'ALT-0065','time':'14:10:00 UTC','type':'LOITERING','title':'Loitering Detected','desc':'Individual stationary >20 min near ATM','cam':'CAM-0112','zone':'Zone 1','sev':'LOW','color':'#ffd700','status':'RESOLVED'},
    ]
    return render(request, 'alerts/index.html', {'alerts': alerts})
