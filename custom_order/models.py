from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CustomShieldOrder(models.Model):
    SHIELD_TYPES = [
        ('SHIELD', 'A knight shield with its coat of arms'),
        ('SADDLE', 'Customizing a horse saddle'),
        ('ENGRAVING', 'Engraving on the blade of a sword'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lord_name = models.CharField(max_length=50)
    shield_type = models.CharField(max_length=20, choices=SHIELD_TYPES, default='SHIELD')
    heraldry_description = models.TextField()
    STATUS_CHOICES = [
        ('WAITING', 'Waiting the blacksmith to start'),
        ('IN_PROGRESS', 'The craftsmen are making'),
        ('READY', 'Ready to ship'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='WAITING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lord_name

    class Meta:
        ordering = ['-id']