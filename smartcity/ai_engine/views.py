from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    models = [
        {'name':'Weapon Detector','type':'YOLOv8','accuracy':'97.3%','status':'ACTIVE','processed_today':14823,'alerts_today':3,'color':'#ff0040'},
        {'name':'Face Recognition','type':'ArcFace','accuracy':'99.1%','status':'ACTIVE','processed_today':28441,'alerts_today':1,'color':'#00f5ff'},
        {'name':'Crowd Density','type':'CSRNet','accuracy':'94.6%','status':'ACTIVE','processed_today':9217,'alerts_today':2,'color':'#ff6b35'},
        {'name':'Anomaly Detect','type':'AutoEncoder','accuracy':'91.2%','status':'ACTIVE','processed_today':31200,'alerts_today':4,'color':'#7c3aed'},
        {'name':'License Plate OCR','type':'EasyOCR','accuracy':'98.8%','status':'ACTIVE','processed_today':5621,'alerts_today':0,'color':'#00ff88'},
        {'name':'Fire & Smoke','type':'ResNet50','accuracy':'96.4%','status':'TRAINING','processed_today':0,'alerts_today':0,'color':'#ffd700'},
    ]
    return render(request, 'ai_engine/index.html', {'models': models, 'total_inferences': 89302})
