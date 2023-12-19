from django.shortcuts import render
import random
from datetime import datetime, timedelta
import time
import json


# Create your views here.
def index(request):
    context = {
        'username': 'niuxiaofu'
    }
    return render(request, "index.html", context=context)


def echarsView(request):
    kpidataList = []
    axis = []
    startTime = '2023-09-07 00:00:00'
    axis.append(startTime)
    for t in range(1441):
        Time = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=(1 * t))
        axis.append(str(Time))
    for i in range(2):
        kpidata = {'axis': axis,
                   'data': [random.randint(1, 100) for i in range(1440)],
                   'total': '交易量' + str(i),
                   'index': i
                   }
        kpidataList.append(kpidata)

    context = {}
    context['list'] = kpidataList
    return render(request, "echart.html", context=context)
