from django.db.models import F
from .models import OperatingSystemStats

class CustomMiddlware:

  def __init__(self, get_response): #required method 
      
    self.get_response = get_response





  def __call__(self, request): #this method is required

    if "admin" not in request.path:          
      self.stats(request.META['HTTP_USER_AGENT'])  #HTTP_USER_AGENT attribute provides information about the operating system ( Client in this case )
      print(request.META['HTTP_USER_AGENT'])
    response = self.get_response(request)

    return response



  def stats(self, os_info): #this is a custom method 
    #here we are checking what is the output for the os_info and increasing the count as required
    # pass
    if "Windows" in os_info:
        OperatingSystemStats.objects.all().update(win=F('win') + 1)
        
    elif "mac" in os_info:
        OperatingSystemStats.objects.all().update(mac=F('mac') + 1)
        
    elif "iPhone" in os_info:
        OperatingSystemStats.objects.all().update(iph=F('iph') + 1)
        
    elif "Android" in os_info:
        OperatingSystemStats.objects.all().update(android=F('android') + 1)
        
    else:
        OperatingSystemStats.objects.all().update(oth=F('oth') + 1)
  






