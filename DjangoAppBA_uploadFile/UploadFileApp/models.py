from django.db import models


class UploadedFile(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
