from django.db import models

class Todo(models.Model):
    task = models.TextField()
    created_at = models.DateField()
    due_at = models.DateField()
    is_completed = models.BooleanField(default = False) 

    #to show object name in place of object(id) in admin page we write
    def __str__(self):
        return self.task + " from " + str(self.created_at) + " to " + str(self.due_at)

class Profile(models.Model): 
    title = models.CharField(max_length = 30)
    profile_pic = models.ImageField(upload_to = "profile_pic/") # have a keyword argument ----> upload_to 