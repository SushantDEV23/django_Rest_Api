from django.db import models

class Drink(models.Model):
    name=models.CharField(max_length=15, null=False)
    type=models.CharField(max_length=15, null=False)
    company=models.CharField(max_length=16)
    desc=models.CharField(max_length=100)

    def __str__(self):
        return self.name+"  --  "+self.desc