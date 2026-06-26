from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.date} {self.time}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=3)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    date_label = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.date_label}"


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('hookah', 'Hookah'),
        ('drinks', 'Drinks'),
        ('food', 'Food'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.category})"
