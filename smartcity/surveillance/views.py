from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    cameras = [
        {
            'id':'CAM-0112',
            'location':'Downtown · Main St',
            'zone':'Zone 1',
            'status':'CLEAR',
            'video_url':'videos/cam1_fixed.mp4'
        },
        {
            'id':'CAM-0247',
            'location':'Harbor · Sector 4',
            'zone':'Zone 2',
            'status':'CLEAR',
            'video_url':'videos/cam2.mp4'
        },
        {
            'id':'CAM-0383',
            'location':'Airport · Terminal B',
            'zone':'Zone 3',
            'status':'ALERT',
            'video_url':'videos/cam3.mp4'
        },
        {
            'id':'CAM-0429',
            'location':'Central Park',
            'zone':'Zone 4',
            'status':'CLEAR',
            'video_url':'videos/cam4.mp4'
        },
        {
            'id':'CAM-0565',
            'location':'Market District',
            'zone':'Zone 5',
            'status':'WATCH',
            'video_url':'videos/cam5.mp4'
        },
        {
            'id':'CAM-0691',
            'location':'Industrial Zone',
            'zone':'Zone 6',
            'status':'CLEAR',
            'video_url':'videos/cam1_fixed.mp4'  # reuse or change
        },
    ]

    return render(request, 'surveillance/index.html', {'cameras': cameras})