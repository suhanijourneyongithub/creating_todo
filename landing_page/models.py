from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)

    task = models.TextField() #isme text type ka data aayega
    created_at = models.DateField() #isme date type ka data aayega
    due_at = models.DateField() #isme bhi date type ka data aayega

    is_completed = models.BooleanField(default = False) 

    #to show object name in place of object(id) in admin page we write
    def __str__(self):
        return self.task + " from " + str(self.created_at) + " to " + str(self.due_at)

class Profile(models.Model): 
    title = models.CharField(max_length = 30)
    profile_pic = models.ImageField(upload_to = "profile_pic/") # have a keyword argument ----> upload_to 