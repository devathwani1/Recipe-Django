from django.db import models

# Create your models here.

class Notes(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.IntegerField()
    student_sem = models.IntegerField()
    student_sub = models.CharField(max_length=100)
    note_desc = models.TextField()
    note_file = models.FileField(upload_to="submit_notes")

    def __str__(self) -> str:
        return self.student_name