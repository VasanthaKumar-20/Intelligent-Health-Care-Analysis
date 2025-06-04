# hospital_app/models.py

from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    total_beds = models.IntegerField()
    vacant_beds = models.IntegerField()

    def __str__(self):
        return self.name
