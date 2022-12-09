from django.db import models
# Create your models here.
class Billform(models.Model):
    name = models.CharField(max_length=30)
    registered_number = models.IntegerField()
    alt_number = models.IntegerField()
    address = models.CharField(max_length=200)
    bill_data = models.DateField()
    total_amount_pending = models.IntegerField()
    amount_paid = models.IntegerField()
    remaining_amount = models.IntegerField()
    billing_address = models.CharField(max_length=200)
    card_no = models.CharField(max_length=30)
    ExpiryDate = models.DateField()
    cvv = models.CharField(max_length=30)
    agent_name = models.CharField(max_length=30)
    query = models.TextField()
    status = models.BooleanField(default=False)


    def __str__(self):
         return self.name
