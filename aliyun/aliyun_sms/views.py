import datetime
import json

import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request,'index.html')

