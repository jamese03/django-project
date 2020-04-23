from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#each attribute is a field in the db
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #also can try auto_now=True within dateTimeField args
    date_posted = models.DateTimeField(default=timezone.now)
    #look into models.SET_DEFAULT( deleted user)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title