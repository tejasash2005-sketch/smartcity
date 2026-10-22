from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    notifs = [
        {'id':1,'time':'14:34 UTC','title':'CRITICAL: Weapon Detected','body':'CAM-0383 · Airport Terminal B — Firearm identified. Units dispatched.','type':'ALERT','read':False,'color':'#ff0040'},
        {'id':2,'time':'14:30 UTC','title':'HIGH: Crowd Surge at Market','body':'CAM-0565 · Market Gate 7 — Density exceeds safe limit.','type':'ALERT','read':False,'color':'#ff0040'},
        {'id':3,'time':'14:18 UTC','title':'Patrol Unit Alpha checked in','body':'Sgt. Priya Shah confirmed arrival at checkpoint Zone 5.','type':'PATROL','read':False,'color':'#00f5ff'},
        {'id':4,'time':'14:05 UTC','title':'Daily Report Ready','body':'Daily Incident Summary for May 1 has been generated.','type':'REPORT','read':True,'color':'#7c3aed'},
        {'id':5,'time':'13:50 UTC','title':'Camera Offline: CAM-0088','body':'Highway 4 Junction 9 — Camera offline. Maintenance alerted.','type':'SYSTEM','read':True,'color':'#ff6b35'},
        {'id':6,'time':'13:30 UTC','title':'INC-0828 Resolved','body':'Graffiti incident at Downtown Main St marked resolved by Cpl. Dev Singh.','type':'INCIDENT','read':True,'color':'#00ff88'},
    ]
    return render(request, 'notifications/index.html', {'notifs': notifs, 'unread': sum(1 for n in notifs if not n['read'])})
