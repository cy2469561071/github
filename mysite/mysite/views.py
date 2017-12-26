from django.http import HttpResponse
import datetime
def hello(request):
	now=datetime.datetime.now()
	html="<html><body>hello world.it is now %s.</body></html>" % now
	return HttpResponse(html)
