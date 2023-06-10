from django.db import models


class ErrorLogs(models.Model):
    name = models.CharField(max_length=100)
    error_code = models.CharField(max_length=20, blank=True, null=True)
    from_api = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField()
    request_data = models.JSONField(blank=True, null=True)
    response_data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
