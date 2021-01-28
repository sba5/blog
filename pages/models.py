from django.db import models

# Create your models here.

class Diary(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="user_id", null=True)
    content = models.CharField(max_length=1000, verbose_name="user_id")
    
    class Meta:
        db_table = "Diaries"
        verbose_name = "Diaries"
        verbose_name_plural = "Diaries"

    def __str__(self):
        return self.content
