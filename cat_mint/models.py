from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid


class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    image_url = models.URLField(max_length=2048) 
    title = models.CharField(max_length=255, blank=True, null=True)


class Cat(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    cat_name = models.CharField(max_length=50 , null=False, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    breed = models.CharField(max_length=50, null=True, blank=True)
    image = models.OneToOneField(Image, on_delete=models.DO_NOTHING, null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    updated_at = models.DateTimeField(blank=False, default=timezone.now, null=False)
    created_at = models.DateTimeField(
        blank=False, default=timezone.now, null=False, editable=False
    )
