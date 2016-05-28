from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.


def search_form(request):
    return render_to_response('templates/search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)