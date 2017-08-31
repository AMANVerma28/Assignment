"""from django.http import HttpResponse,Http404
import datetime

def hello(request):
	return HttpResponse("Hello World!")

def print_date(request):
	now=datetime.datetime.now()
	html="<html><body>The current date and time is %s</body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset=int(offset)
	except ValueError:
		raise Http404()
	dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
	html="<html><body>In %s hours, the time will be %s</body></html>" %(offset,dt)
	return HttpResponse(html) """
	