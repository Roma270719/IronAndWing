from django.db import models

class Navbar(models.Model):
    name = models.CharField(max_length=50)
    main = models.CharField(max_length=50)
    catalog = models.CharField(max_length=50)
    info = models.CharField(max_length=50)
    custom = models.CharField(max_length=50)

    def __str__(self):
        return "NavBar"


class AboutInfo(models.Model):
    headline = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField()
    footer_one = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    footer_text = models.TextField(null=True, blank=True)
    footer_three = models.CharField(max_length=50, null=True, blank=True)
    footer_work = models.CharField(max_length=50, null=True, blank=True)
    footer_time = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "About Us"

    class Meta:
        verbose_name_plural = "About Us"


class Feedback(models.Model):
    headline = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback Messages"