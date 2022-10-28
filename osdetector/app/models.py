from django.db import models

class OperatingSystemStats(models.Model):
  win = models.IntegerField()
  mac = models.IntegerField()
  iph = models.IntegerField()
  android = models.IntegerField()
  oth = models.IntegerField()