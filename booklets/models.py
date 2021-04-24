from django.db import models
from django.contrib.auth.models import User
import uuid

#validation momkn tb2a fel model bt3 el category mn 3'er form 
class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"
   
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Isbn(models.Model):
    author_title=models.CharField(max_length=50,null=True,blank=True)
    isbn_number=models.UUIDField(default = uuid.uuid4,editable = False)

    def __str__(self):
        return f"{self.isbn_number} isbn_number"

class Summary(models.Model):
    description=models.CharField(max_length=1048)
    
    def __str__(self):
        return self.description

class Booklet(models.Model):
    title=models.CharField(max_length=255,null="True",blank="True")
    content=models.TextField(max_length=2048,null="True",blank="True")
    categories=models.ManyToManyField(Category)
    author=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name="booklets")
    isbn=models.OneToOneField(Isbn,on_delete=models.CASCADE,null=True,blank=True)
    summary=models.ForeignKey(Summary,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

