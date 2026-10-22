from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    logs = [
        {'id':901,'time':'14:34:12','user':'TEJASASH@2005','action':'VIEW','resource':'Dashboard','ip':'127.0.0.1','status':'OK'},
        {'id':900,'time':'14:30:45','user':'TEJASASH@2005','action':'ACCESS','resource':'Alert ALT-0071','ip':'127.0.0.1','status':'OK'},
        {'id':899,'time':'14:28:02','user':'LT.KUMAR','action':'UPDATE','resource':'Incident INC-0831','ip':'10.0.0.5','status':'OK'},
        {'id':898,'time':'14:22:18','user':'SGT.SHAH','action':'VIEW','resource':'Evidence EVD-0439','ip':'10.0.0.8','status':'OK'},
        {'id':897,'time':'14:15:33','user':'CPL.MEHTA','action':'DOWNLOAD','resource':'Report RPT-0126','ip':'10.0.0.12','status':'OK'},
        {'id':896,'time':'14:10:00','user':'UNKNOWN','action':'LOGIN','resource':'accounts/login','ip':'192.168.1.44','status':'FAIL'},
        {'id':895,'time':'14:08:12','user':'TEJASASH@2005','action':'LOGIN','resource':'accounts/login','ip':'127.0.0.1','status':'OK'},
        {'id':894,'time':'13:55:30','user':'CONST.NAIR','action':'VIEW','resource':'Cameras','ip':'10.0.0.9','status':'OK'},
        {'id':893,'time':'13:30:00','user':'CPL.SINGH','action':'CLOSE','resource':'Incident INC-0828','ip':'10.0.0.11','status':'OK'},
    ]
    return render(request, 'audit/index.html', {'logs': logs})
