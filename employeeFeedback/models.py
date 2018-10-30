from datetime import datetime
from django.db import models


class CustomModel(models.Model):
    createdAt = models.DateTimeField(default=datetime.now())
    modifiedAt = models.DateTimeField(default=datetime.now())
    isDeleted = models.BooleanField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id or not self.createdAt:
            self.createdAt = datetime.now()
        self.modifiedAt = datetime.now()
        super(CustomModel, self).save(*args, **kwargs)

    def delete(self):
        self.isDeleted = True
        super(CustomModel, self).save()

    def hardDelete(self):
        super(CustomModel, self).delete(self)


class Employee(CustomModel):
    empId = models.TextField(unique=True)
    empName = models.TextField(blank=False)
    designation = models.TextField(null=True)
    joiningDate = models.DateTimeField(null=True)
    mobileNumber = models.CharField(max_length=20, null=True)
    empEmail = models.EmailField(unique=True, db_index=True, max_length=255)
    address = models.TextField(null=True)
