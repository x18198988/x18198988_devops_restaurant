from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models hec
class Typ(models.Model):
    name=models.CharField(max_length=40)
    floor=models.CharField(max_length=20)

class Table(models.Model):
    seats=models.CharField(max_length=40)
    typ=models.ForeignKey(Typ, on_delete=models.PROTECT)

class Booking(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    table=models.ForeignKey(Table, on_delete=models.PROTECT)    
    date_time=models.DateTimeField(auto_now_add=True)
    sr=models.TextField()