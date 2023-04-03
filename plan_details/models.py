from django.db import models

# Create your models here.

class Plan(models.Model):
    #Personal Info
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    
    
    #Plan Selection
    PLAN_CHOICES = (
        (1, 'Arcade'),
        (2, 'Advanced'),
        (3, 'Pro'),
        
    )

    plan_name = models.CharField(max_length=10, choices=PLAN_CHOICES, default=1)
    plan_duration_is_monthly = models.BooleanField(default=True)
    online_service = models.BooleanField(default=False)
    larger_storage = models.BooleanField(default=False)
    customizable_profile = models.BooleanField(default=False)
    total_cost = models.IntegerField(default=9)
    
    def __str__(self):
        return self.plan_name
