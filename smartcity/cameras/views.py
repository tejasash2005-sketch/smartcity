from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

@login_required
def index(request):
    cameras = [
        {
            'id':'CAM-0112',
            'location':'Downtown · Main St',
            'status':'ONLINE',
            'video_url': static('videos/cam1_fixed.mp4')
        },
        {
            'id':'CAM-0247',
            'location':'Harbor · Sector 4',
            'status':'ONLINE',
            'video_url': static('videos/cam2.mp4')
        },
        {
            'id':'CAM-0383',
            'location':'Airport · Terminal B',
            'status':'ALERT',
            'video_url': static('videos/cam3.mp4')
        },
        {
            'id':'CAM-0429',
            'location':'Central Park',
            'status':'ONLINE',
            'video_url': static('videos/cam4.mp4')
        },
        {
            'id':'CAM-0512',
            'location':'Parking Block B',
            'status':'ONLINE',
            'video_url': static('videos/cam5.mp4')
        },
        {
            'id':'CAM-0565',
            'location':'Market District',
            'status':'WATCH',
            'video_url': static('videos/cam1_fixed.mp4')
        },
        {
            'id':'CAM-0691',
            'location':'Industrial Zone',
            'status':'ONLINE',
            'video_url': static('videos/cam2.mp4')
        },
        {
            'id':'CAM-0083',
            'location':'Central Stn · P3',
            'status':'ONLINE',
            'video_url': static('videos/cam3.mp4')
        },
        {
            'id':'CAM-0088',
            'location':'Highway 4 · J9',
            'status':'OFFLINE',
            'video_url': static('videos/cam4.mp4')
        },
    ]

    return render(request, 'cameras/index.html', {
        'cameras': cameras,
        'total': len(cameras),
        'online': sum(1 for c in cameras if c['status'] in ['ONLINE','WATCH','ALERT'])
    })