from django.db import models

# Create your models here.
# Note model is created with id as primary key, title as char field and content as text field.
class Note(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)