from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class People(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100, null=False, blank=False)
    inn = models.CharField(verbose_name='ИНН', max_length=12, null=False, blank=False)
    age = models.IntegerField(verbose_name="Возраст", default=None, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Change date', auto_now_add=True)
    deleted_at = models.DateTimeField(verbose_name="Delete date", null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Deleted", default=False, null=False)

    def __str__(self) -> str:
        return f"{self.name} - {self.inn}"
    
    def delete(self, using=None, keep_parents = False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

        
            
