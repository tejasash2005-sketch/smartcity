from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items = [
        {'id':'EVD-0441','incident':'INC-0831','type':'VIDEO','title':'Suspicious Package Footage','cam':'CAM-0083','date':'2026-05-01 14:32','size':'2.4 GB','status':'SEALED','icon':'🎬'},
        {'id':'EVD-0440','incident':'INC-0830','type':'IMAGE','title':'Crowd Surge Screenshots','cam':'CAM-0247','date':'2026-05-01 14:18','size':'18.2 MB','status':'PROCESSING','icon':'🖼️'},
        {'id':'EVD-0439','incident':'INC-0826','type':'VIDEO','title':'Weapon Detection Clip','cam':'CAM-0383','date':'2026-05-01 11:42','size':'1.1 GB','status':'SEALED','icon':'🎬'},
        {'id':'EVD-0438','incident':'INC-0829','type':'IMAGE','title':'Vehicle Break-In Photos','cam':'CAM-0512','date':'2026-05-01 13:55','size':'45.8 MB','status':'AVAILABLE','icon':'🖼️'},
        {'id':'EVD-0437','incident':'INC-0828','type':'VIDEO','title':'Graffiti Incident Clip','cam':'CAM-0112','date':'2026-05-01 13:30','size':'340 MB','status':'AVAILABLE','icon':'🎬'},
        {'id':'EVD-0436','incident':'INC-0825','type':'VIDEO','title':'Night Loitering Footage','cam':'CAM-0691','date':'2026-04-30 23:15','size':'890 MB','status':'AVAILABLE','icon':'🎬'},
    ]
    return render(request, 'evidence/index.html', {'items': items})
