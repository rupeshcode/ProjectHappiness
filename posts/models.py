from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission, User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


# Create your models here.
# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)

class Story(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # text = body
    story = models.TextField()
    title = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,)
    isModerated = models.BooleanField(default=False, null=False)
    responsesRequired = models.BooleanField(default=False, null=False)

    #    class Meta:
    #        db_table = "questions"
    #        verbose_name = ("Question")
    #        verbose_name_plural = ("Questions")
    #        ordering = ("created_date")
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)



    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Story.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.created_date = timezone.now
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Story, self).save(*args, **kwargs)


class Response(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.CharField(max_length=1000)
    # date = models.DateTimeField(auto_now_add=True)
    isModerated = models.BooleanField(default=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        self.created_date = timezone.now()
        super(Response, self).save(*args, **kwargs)
