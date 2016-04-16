from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime
import MySQLdb

def hello(request):
    return HttpResponse("Hello world!")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'dateapp/current_datetime.html', {'current_date':now})
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date':now}))

    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)