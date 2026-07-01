from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class GuildProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField(blank=True, null=True)
    material_or_element = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    stock_change = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Add/Remove Stock (e.g. +142 or -5)",
        help_text="Enter a positive number to add, or a negative number to subtract from current stock."
    )
    image = models.ImageField(upload_to='products_images/', verbose_name="Product Image", blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.stock is None:
            self.stock = 0

        if self.stock_change:
            self.stock += self.stock_change
            self.stock_change = 0

        super().save(*args, **kwargs)



class BattleReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(GuildProduct, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.product.name} ({self.rating}★)"

    class Meta:
        ordering = ['-id']
