from django.contrib import admin
from .models import Question,Response
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import Profile

# Register your models here.

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('profile','question','response')
    search_fields = ['profile__user__username','question__ques_round','response',]
    list_filter = ('profile','question')

admin.site.register(Question)
admin.site.register(Response, ResponseAdmin)
