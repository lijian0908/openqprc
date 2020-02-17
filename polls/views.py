from django.http import HttpResponse
from .models import user

# Create your views here.

def index(request):

    users = user.objects.all()
    user_list = ','.join([q.user_name+":"+str(q.age) for q in users])
    return HttpResponse(user_list)