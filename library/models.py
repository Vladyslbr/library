from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Document(models.Model):
    name = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='documents/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents', null=True)

    class Meta:
        ordering = ['-upload_date']
        indexes = [models.Index(fields=['-upload_date']), ]

    def __str__(self):
        return self.name

