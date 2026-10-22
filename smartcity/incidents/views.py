from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    incidents = [
        {'id':'INC-0831','date':'2026-05-01','time':'14:32','title':'Suspicious Package','location':'Central Station · Platform 3','cam':'CAM-0083','officer':'Cpl. Ravi Mehta','sev':'HIGH','status':'OPEN','type':'Security'},
        {'id':'INC-0830','date':'2026-05-01','time':'14:18','title':'Crowd Surge Alert','location':'Market District · Gate 7','cam':'CAM-0247','officer':'Sgt. Priya Shah','sev':'HIGH','status':'INVESTIGATING','type':'Crowd'},
        {'id':'INC-0829','date':'2026-05-01','time':'13:55','title':'Vehicle Break-In','location':'Parking Zone B · Level 2','cam':'CAM-0512','officer':'Const. Arjun Nair','sev':'MED','status':'INVESTIGATING','type':'Theft'},
        {'id':'INC-0828','date':'2026-05-01','time':'13:30','title':'Graffiti Detected','location':'Downtown · Main St Wall','cam':'CAM-0112','officer':'Cpl. Dev Singh','sev':'LOW','status':'RESOLVED','type':'Vandalism'},
        {'id':'INC-0827','date':'2026-05-01','time':'12:58','title':'Traffic Obstruction','location':'Highway 4 · Junction 9','cam':'CAM-0389','officer':'Sgt. Anika Roy','sev':'LOW','status':'RESOLVED','type':'Traffic'},
        {'id':'INC-0826','date':'2026-05-01','time':'11:42','title':'Weapon Detected','location':'Airport · Terminal B','cam':'CAM-0383','officer':'Lt. Suresh Kumar','sev':'CRITICAL','status':'RESOLVED','type':'Security'},
        {'id':'INC-0825','date':'2026-04-30','time':'23:15','title':'Night Loitering','location':'Industrial Zone','cam':'CAM-0691','officer':'Const. Meera Patel','sev':'LOW','status':'RESOLVED','type':'Loitering'},
    ]
    return render(request, 'incidents/index.html', {'incidents': incidents})
