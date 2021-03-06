from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField
from django.contrib.auth.models import User

from website.apps.profiles.models import Profile
    

# Generic alert model
class Alert(models.Model):
    
    read = models.BooleanField(default=False)
    title = models.TextField(max_length = 200, blank = True, default='', null=True)
    message = models.TextField(max_length = 200, blank = True, default='', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Alert constructor
    @classmethod
    def create(cls, title, message, user):
        alert = cls(title=title,
                    message = message,
                    user = user)
        alert.save()
        return alert