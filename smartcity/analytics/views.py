from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    ctx = {
        'total_incidents': 38,
        'resolved_pct': 74,
        'avg_response': '4.2 min',
        'hotspot': 'Zone 5',
        'weekly': [24, 31, 28, 35, 42, 38, 38],
        'by_type': [
            {'type':'Security','count':12,'pct':31,'color':'#ff0040'},
            {'type':'Traffic','count':9,'pct':24,'color':'#ff6b35'},
            {'type':'Crowd','count':7,'pct':18,'color':'#ffd700'},
            {'type':'Theft','count':6,'pct':16,'color':'#7c3aed'},
            {'type':'Other','count':4,'pct':11,'color':'#7d8590'},
        ],
        'zones': [
            {'name':'Zone 1 · Downtown','incidents':8,'cameras':142},
            {'name':'Zone 2 · Harbor','incidents':4,'cameras':98},
            {'name':'Zone 3 · Airport','incidents':11,'cameras':201},
            {'name':'Zone 4 · Central Park','incidents':3,'cameras':87},
            {'name':'Zone 5 · Market','incidents':9,'cameras':156},
            {'name':'Zone 6 · Industrial','incidents':3,'cameras':112},
        ]
    }
    return render(request, 'analytics/index.html', ctx)
