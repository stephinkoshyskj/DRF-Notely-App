from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone = models.CharField(max_length=200,unique=True) # added by user

class Task(models.Model):
    
    title = models.CharField(max_length=200)

    description = models.TextField()

    status_chocies = (
        ("pending", "pending"),
        ("in-progress", "in-progress"),
        ("done", "done")
    )

    status = models.CharField(max_length=200,
                              choices=status_chocies,
                              default="pending")
    
    created_date = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    category_choices = (
        ("business", "business"),
        ("personal", "personal"),
    )

    category = models.CharField(max_length=200,
                                choices=category_choices,
                                default="personal"
                                )
    
    priority_choices = (
        ("low", "low"),
        ("medium", "medium"),
        ("high", "high"),
    )

    priority = models.CharField(max_length=200,
                                choices=priority_choices,
                                default="low")
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
