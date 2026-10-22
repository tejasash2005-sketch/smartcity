from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    reports = [
        {'id':'RPT-0128','title':'Daily Incident Summary — May 1','type':'DAILY','generated':'2026-05-01 06:00','by':'Auto-System','status':'READY','pages':8},
        {'id':'RPT-0127','title':'Weekly Crime Trend Report — Wk 18','type':'WEEKLY','generated':'2026-04-27 08:00','by':'Lt. Suresh Kumar','status':'READY','pages':22},
        {'id':'RPT-0126','title':'Zone 3 Airport Security Audit','type':'AUDIT','generated':'2026-04-26 14:30','by':'Sgt. Priya Shah','status':'READY','pages':15},
        {'id':'RPT-0125','title':'Monthly Analytics — April 2026','type':'MONTHLY','generated':'2026-05-01 07:00','by':'Auto-System','status':'READY','pages':40},
        {'id':'RPT-0124','title':'Incident Escalation Report — INC-0826','type':'INCIDENT','generated':'2026-05-01 12:00','by':'Cpl. Ravi Mehta','status':'DRAFT','pages':5},
    ]
    return render(request, 'reports/index.html', {'reports': reports})
