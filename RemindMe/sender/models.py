from django.db import models


# Create your models here.
from django.db import models
from django.core.validators import EmailValidator


class EmailMessage(models.Model):
    recipient_email = models.EmailField(
        validators=[EmailValidator()], verbose_name="To"
    )
    subject = models.CharField(max_length=200)
    scheduled_time = models.DateTimeField(verbose_name="Time")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Email to {self.recipient_email} - {self.subject}"
