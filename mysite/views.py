from django.http import HttpResponse
from django.template import Template,Context
import datetime as dt

def hello(request):
    return HttpResponse("Hello world!")


def self_introduction(request):
    fp=open('/home/zyy666/mysite/static/self-introduction.html')
    t=Template(fp.read())
    fp.close()
    html=t.render(Context())
    return HttpResponse(html)


