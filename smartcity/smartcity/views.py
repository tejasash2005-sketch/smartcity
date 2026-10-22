from django.shortcuts import render

def homepage(request):
    stats = {
        'cameras_online': 1247,
        'incidents_today': 38,
        'alerts_active': 12,
        'areas_covered': 94,
    }
    modules = [
        {'name': 'Live Surveillance', 'icon': 'camera', 'desc': 'Real-time AI camera feeds', 'url': '/surveillance/', 'color': '#00f5ff', 'tag': 'LIVE'},
        {'name': 'Police Dashboard', 'icon': 'shield', 'desc': 'Command center for law enforcement', 'url': '/dashboard/', 'color': '#ff6b35', 'tag': 'CMD'},
        {'name': 'Alert System', 'icon': 'bell', 'desc': 'Automated threat detection & alerts', 'url': '/alerts/', 'color': '#ff0040', 'tag': 'HOT'},
        {'name': 'Camera Network', 'icon': 'video', 'desc': 'Manage 1,247 city camera nodes', 'url': '/cameras/', 'color': '#7c3aed', 'tag': None},
        {'name': 'Analytics Hub', 'icon': 'bar-chart-2', 'desc': 'Crime patterns & predictive analytics', 'url': '/analytics/', 'color': '#059669', 'tag': 'AI'},
        {'name': 'Incident Reports', 'icon': 'file-text', 'desc': 'Document and track all incidents', 'url': '/incidents/', 'color': '#d97706', 'tag': None},
        {'name': 'Report Generator', 'icon': 'printer', 'desc': 'Automated daily/weekly reports', 'url': '/reports/', 'color': '#0284c7', 'tag': None},
        {'name': 'Patrol Management', 'icon': 'map', 'desc': 'Officer routing & patrol tracking', 'url': '/patrol/', 'color': '#7c3aed', 'tag': None},
        {'name': 'Evidence Vault', 'icon': 'lock', 'desc': 'Secure video & image evidence', 'url': '/evidence/', 'color': '#dc2626', 'tag': 'SEC'},
        {'name': 'City Map', 'icon': 'globe', 'desc': 'Live threat heatmap & zones', 'url': '/map/', 'color': '#0891b2', 'tag': 'GEO'},
        {'name': 'Face Recognition', 'icon': 'user-check', 'desc': 'AI-powered facial identification', 'url': '/ai/', 'color': '#4f46e5', 'tag': 'AI'},
        {'name': 'Object Detection', 'icon': 'crosshair', 'desc': 'YOLO weapon & threat detection', 'url': '/ai/', 'color': '#be123c', 'tag': 'AI'},
        {'name': 'Notifications', 'icon': 'send', 'desc': 'Multi-channel alert dispatch', 'url': '/notifications/', 'color': '#b45309', 'tag': None},
        {'name': 'Audit Logs', 'icon': 'clipboard', 'desc': 'Full system access audit trail', 'url': '/audit/', 'color': '#475569', 'tag': None},
        {'name': 'AI Engine', 'icon': 'cpu', 'desc': 'Configure ML models & thresholds', 'url': '/ai/', 'color': '#06b6d4', 'tag': 'ML'},
        {'name': 'Suspect Database', 'icon': 'database', 'desc': 'Watchlist & criminal records', 'url': '/surveillance/', 'color': '#7c2d12', 'tag': None},
        {'name': 'Traffic Monitor', 'icon': 'activity', 'desc': 'Traffic flow & accident detection', 'url': '/surveillance/', 'color': '#15803d', 'tag': 'LIVE'},
        {'name': 'Emergency Response', 'icon': 'alert-triangle', 'desc': 'SOS dispatch & coordination', 'url': '/alerts/', 'color': '#ef4444', 'tag': 'SOS'},
        {'name': 'System Settings', 'icon': 'settings', 'desc': 'Configure system parameters', 'url': '/settings/', 'color': '#6b7280', 'tag': None},
        {'name': 'Drone Control', 'icon': 'navigation', 'desc': 'Aerial surveillance management', 'url': '/surveillance/', 'color': '#8b5cf6', 'tag': 'UAV'},
    ]
    return render(request, 'home.html', {'stats': stats, 'modules': modules})
