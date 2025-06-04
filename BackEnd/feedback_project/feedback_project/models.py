from django.db import models

class Feedback(models.Model):
    patient_name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=100)
    disease = models.CharField(max_length=50)
    surgeon_name = models.CharField(max_length=100)
    treatment_date = models.DateField()
    treatment_cost = models.DecimalField(max_digits=10, decimal_places=2)
    feedback_score = models.IntegerField()
    recovered = models.CharField(max_length=10)  # Yes or No
    comments = models.TextField()

    class Meta:
        app_label = 'feedback_project'

    def __str__(self):
        return f"{self.patient_name} - {self.hospital_name}"
