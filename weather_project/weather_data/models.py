
from django.db import models


class WeatherRecord(models.Model):
    region = models.CharField(max_length=50, null=True)
    parameter = models.CharField(max_length=50, null=True)
    year = models.IntegerField()
    jan = models.FloatField(null=True)
    feb = models.FloatField(null=True)
    mar = models.FloatField(null=True)
    apr = models.FloatField(null=True)
    may = models.FloatField(null=True)
    jun = models.FloatField(null=True)
    jul = models.FloatField(null=True)
    aug = models.FloatField(null=True)
    sep = models.FloatField(null=True)
    oct = models.FloatField(null=True)
    nov = models.FloatField(null=True)
    dec = models.FloatField(null=True)
    annual = models.FloatField(null=True)

    def __str__(self):
        return f"{self.region} - {self.parameter} - {self.year}"






# class WeatherRecord(models.Model):
#     year = models.IntegerField()
#     jan = models.FloatField(null=True)
#     feb = models.FloatField(null=True)
#     mar = models.FloatField(null=True)
#     apr = models.FloatField(null=True)
#     may = models.FloatField(null=True)
#     jun = models.FloatField(null=True)
#     jul = models.FloatField(null=True)
#     aug = models.FloatField(null=True)
#     sep = models.FloatField(null=True)
#     oct = models.FloatField(null=True)
#     nov = models.FloatField(null=True)
#     dec = models.FloatField(null=True)
#     annual = models.FloatField(null=True)

#     def __str__(self):
#         return str(self.year)
    