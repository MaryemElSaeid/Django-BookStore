from django.db import models
 
class Booklet(models.Model):
    title=models.CharField(max_length=255,null="True",blank="True")
    content=models.TextField(max_length=2048)
    def __str__(self):
        return self.title

