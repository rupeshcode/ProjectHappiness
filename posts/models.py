from django.db import models
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField #does not contain upload option for us in Images
from ckeditor_uploader.fields import  RichTextUploadingField #for adding upload from our own server in CKEDITOR
from django.template.defaultfilters import slugify
import datetime
from django.utils import timezone
# Create your models here.
#user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male','M'),
        ('Female','F' ),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    bio  = models.CharField(blank=True, max_length=200,null=True)
    gender = models.CharField(max_length=128, choices=GENDER_CHOICES,null=True,blank=True)
    dob = models.DateTimeField(blank=True, null=True)
    image = models.FileField(null=True,default='Images/No-img.jpg')
    #image  = models.ImageField(upload_to="Images/",default='Images/No-img.jpg',null=True)


    def get_date(self):
        return self.modified.date()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Story(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # text = body
    text = models.TextField()
    title = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False, null=False)
    response_wanted = models.BooleanField(default=False, null=False)
#    class Meta:
#        db_table = "questions"
#        verbose_name = ("Question")
#        verbose_name_plural = ("Questions")
#        ordering = ("created_date")
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.created_date = timezone.now()
        self.save(*args, **kwargs)

class Response(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        self.created_date = timezone.now()
        self.save(*args, **kwargs)