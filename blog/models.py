import os
import uuid
from datetime import date
from django.db import models
from django.conf import settings
from account.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save, post_delete
from django.utils.safestring import mark_safe


class Tag(models.Model):
    value = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return f"#{self.value}"

    class Meta:
        db_table = "tags"


class Post(models.Model):
    def image_path(self, file_name):
        ext = file_name.split(".")[-1]
        path = date.strftime(date.today(), "post/%Y/%m/%d")
        return f"{path}/{os.urandom(64).hex()}.{ext}"

    image = models.ImageField(upload_to=image_path)
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.BigIntegerField(validators=[], default=0)
    text = models.TextField()
    short_desc = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="posts")

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        ordering = ("-created", "-id")

    def admin_img(self):
        return mark_safe('<img src="{}" width="200px" />'.format(self.image.url))

    admin_img.short_description = "Image"
    admin_img.allow_tags = True


# @receiver(pre_save, sender=Post)
# def resave_media(sender, instance, **kwargs):
#     if instance.id is not None


@receiver(post_delete, sender=Post)
def remove_media(sender, instance, **kwargs):
    try:
        path_to_file = settings.MEDIA_ROOT / str(instance.image.path)
        path_to_file.unlink()
    except (OSError, ValueError) as error:
        print(error)
    while True:
        try:
            path_to_file = path_to_file.parent.absolute()
            path_to_file.rmdir()
        except (OSError, ValueError, UnboundLocalError):
            break


@receiver(pre_save, sender=Post)
def set_slug(sender, instance, **kwargs):
    if instance.id is None:
        instance.slug = str(uuid.uuid4())
