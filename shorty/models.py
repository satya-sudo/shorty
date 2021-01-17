from django.db import models

class UrlLink(models.Model):
    short_url = models.CharField(max_length=12,unique=True)
    long_url = models.URLField(unique=False)

    def __str__(self):
        return f"Token:{self.short_url} and long_url:{self.long_url}"
