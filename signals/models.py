from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify

# signals imports
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed,
)

User = settings.AUTH_USER_MODEL



@receiver(pre_save, sender=User)
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    before saved in the database
    """
    print(instance.username, instance.id) # None
    # trigger pre_save
    # DONT DO THIS -> instance.save()
    # trigger post_save

# pre_save.connect(user_created_handler, sender=User)


@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """
    if created:
        print("Send email to", instance.username)
        # trigger pre_save
        # instance.save()
        # trigger post_save
    else:
        print(instance.username, "was just saved")

# post_save.connect(user_created_handler, sender=User)

class Userdetails(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=False)
    department = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    slug= models.SlugField(blank=True, null=True)
    entry_timestamp=models.DateTimeField(blank = True,null=True)


@receiver(pre_save, sender=Userdetails)
def Userdetails_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

@receiver(post_save, sender=Userdetails)
def Userdetails_post_save(sender, instance, created, *args, **kwargs):
    if instance.department:
        print("Departments")
        instance.department = False
        instance.entry_timestamp = timezone.now()
        instance.save()
