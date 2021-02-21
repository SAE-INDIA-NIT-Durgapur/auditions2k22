from django.shortcuts import render
from accounts.models import Profile
from response.models import Response

# Create your views here.

def index(request):
    not_evaluated = Profile.objects.filter(current_status = 1)
    evaluated = Profile.objects.filter(current_status = 2)
    eliminated = Profile.objects.filter(current_status = 3)
    data = {}
    data['not_evaluated'] = not_evaluated
    data['evaluated'] = evaluated
    data['eliminated'] = eliminated
    return render(request,'administrator/dashboard.html',{'data':data})

def response_detail(request,id):
    profile = Profile.objects.get(id = id)
    response = Response.objects.filter(profile = profile)
    data = {}
    data['profile'] = profile
    data['response'] = response
    return render(request,'administrator/detail.html',{'data':data})
