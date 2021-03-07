from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime, timedelta
from dateutil import tz

from django.conf import settings

# Create your models here.
class Profile(models.Model):
    status = [
        (1,'NOT_EVALUATED'),
        (2,'EVALUATED'),
        (3,'ELIMINATED'),
    ]

    user = models.OneToOneField(User,on_delete=CASCADE)
    curr_round = models.IntegerField(default=1)
    current_status = models.IntegerField(choices=status,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    def get_completion_time(self):
        two_hours_from_now = self.created_at + timedelta(hours=2)
        ist = two_hours_from_now.astimezone(tz.tzlocal())
        date_data = {
            'year':ist.year,
            'month':ist.month,
            'day':ist.day,
            'hours' : ist.hour,
            'mins': ist.minute,
            'seconds':ist.second
        }
        return date_data


from django.dispatch import receiver
from django.db.models.signals import post_save
 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
        print(profile.get_completion_time())


