from django.db import models
class Dealer(models.Model):
    name=models.CharField(max_length=120)
    city=models.CharField(max_length=80)
    state=models.CharField(max_length=80)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=30)
    image=models.URLField(blank=True)
    def __str__(self): return self.name

class Review(models.Model):
    dealer=models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name="reviews")
    username=models.CharField(max_length=80)
    text=models.TextField()
    sentiment=models.CharField(max_length=20,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class CarMake(models.Model):
    make=models.CharField(max_length=80)
    models=models.JSONField(default=list)
