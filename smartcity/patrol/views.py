from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    officers = [
        {'id':'P-001','name':'Sgt. Priya Shah','badge':'B-1142','zone':'Zone 5 · Market','status':'ON PATROL','last_check':'14:30 UTC','incidents':2},
        {'id':'P-002','name':'Cpl. Ravi Mehta','badge':'B-0873','zone':'Zone 3 · Airport','status':'ON PATROL','last_check':'14:28 UTC','incidents':5},
        {'id':'P-003','name':'Const. Arjun Nair','badge':'B-2201','zone':'Zone 1 · Downtown','status':'ON BREAK','last_check':'14:10 UTC','incidents':1},
        {'id':'P-004','name':'Lt. Suresh Kumar','badge':'B-0541','zone':'Zone 6 · Industrial','status':'ON PATROL','last_check':'14:32 UTC','incidents':0},
        {'id':'P-005','name':'Sgt. Anika Roy','badge':'B-0987','zone':'Zone 2 · Harbor','status':'ON PATROL','last_check':'14:25 UTC','incidents':1},
        {'id':'P-006','name':'Const. Meera Patel','badge':'B-1885','zone':'Zone 4 · Park','status':'STANDBY','last_check':'13:55 UTC','incidents':0},
    ]
    return render(request, 'patrol/index.html', {'officers': officers, 'active': sum(1 for o in officers if 'PATROL' in o['status'])})
