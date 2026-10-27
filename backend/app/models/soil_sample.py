from django.db import models
from .users import User

class SoilSample(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="soil_samples"
    )

    sample_name=models.CharField(max_length=100)
    crop_name=models.CharField(max_length=100,null=True,blank=True)
    crop_age=models.CharField(max_length=100,null=True,blank=True)
    field_image=models.ImageField(null=True,blank=True)
    user_problem=models.CharField(max_length=250,null=True,blank=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    latitude=models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)
    longitude=models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)
    ph=models.DecimalField(max_digits=4,decimal_places=2)
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    moisture = models.FloatField()
    temperature = models.FloatField()
    ec = models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="soil_sample"
        ordering=["-created_at"]

    def __str__(self):
        return f"{self.sample_name} ({self.user.username})"