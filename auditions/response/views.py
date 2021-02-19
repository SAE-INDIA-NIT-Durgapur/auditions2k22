from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import Question,Response
from accounts.models import Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def get_question(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    if(request.method == 'POST'):
        pass
    else:
        pass
