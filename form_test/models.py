from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()


class PriorHealthPlanModel(models.Model):
    insurer = models.CharField(max_length=100)
    health_plan_name = models.CharField(max_length=20)
    your_name = models.CharField(max_length=100, blank=True)
    member_id = models.CharField(max_length=10)
    subscriber_id = models.CharField(max_length=10)
    group_id = models.CharField(max_length=10)
    plan_id = models.CharField(max_length=10)


class ConsentDateModel(models.Model):
    data_categories_to_fetch = models.CharField(max_length=100)
    date = models.DateField()
    signature_url = models.CharField(max_length=100)
