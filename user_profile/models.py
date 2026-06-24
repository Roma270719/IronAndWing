from django.contrib.auth.models import User
from django.db import models
from catalog.models import GuildProduct


# Create your models here.
class SupplyOrder(models.Model):
    STATUS_CHOICES = [
        ('PREPARING', 'Preparing to ship'),
        ('IN_TRANSIT', 'Caravan on the way'),
        ('DELIVERED', 'Delivered to the castle'),
    ]
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(GuildProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    castle_address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PREPARING')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    class Meta:
        ordering = ['-id']