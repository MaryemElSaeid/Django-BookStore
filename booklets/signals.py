from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver
from .models import Booklet,Isbn,User
 
@receiver(post_save,sender=Booklet)
def after_booklet_creation(sender,instance,created,*args,**KWargs):
    if created:
        isbn_instance=Isbn.objects.create(author_title=instance.author)
        instance.isbn=isbn_instance
        instance.save()
 
    else:
        print("updating")