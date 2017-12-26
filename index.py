import os  

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'  




  
from django.core.wsgi import get_wsgi_application  
from bae.core.wsgi import WSGIApplication  
application = WSGIApplication(get_wsgi_application())  

