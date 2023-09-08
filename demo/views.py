from django.shortcuts import render
import random
import json

# Create your views here.
def index(request):
    context = {
        'username': 'niuxiaofu'
    }
    return render(request, "index.html", context=context)


def echarsView(request):
    kpidataList = []
    for i in range(2):
        kpidata = {'axis': [i for i in range(1440)],
                   'data': [random.randint(1, 100) for i in range(1440)],
                   'total': '交易量' + str(i),
                   'index': i
                   }
        kpidataList.append(kpidata)

    context = {}
    context['list'] = kpidataList
    return render(request, "echart.html", context=context)
