from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Purchases(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    quantity = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField(verbose_name="Total amount")
    date = models.DateField(verbose_name="Date of purchase")

    class Meta:
        verbose_name_plural = "Purchases"

    def __str__(self):
        return self.name + " - " + str(self.quantity)


class Services(models.Model):
    name = models.CharField(max_length=200, verbose_name="Service name")
    amount = models.CharField(max_length=500, verbose_name="Service amount range")
    date = models.DateField(auto_now_add=True, verbose_name="Date registered")

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name+" - "+str(self.amount)


class ServiceOffered(models.Model):
    name = models.CharField(max_length=200, verbose_name="Customer name")
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, verbose_name="Service offered")
    amount = models.PositiveIntegerField(verbose_name="Total amount")
    date = models.DateField(verbose_name="Date of delivery")
    payment = models.BooleanField(default=False, verbose_name="payed")

    @property
    def payment_status(self):
        if self.payment:
            return "Payed"
        else:
            return "Not payed"

    class Meta:
        verbose_name_plural = "Services done"

    def __str__(self):
        return self.name

class Bookings(models.Model):
    name = models.CharField(max_length=200, verbose_name="Customer name")
    date = models.DateField(verbose_name="Date of service")
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Bookings"

    @property
    def completed_status(self):
        if self.status:
            return "completed"
        else:
            return "Active"

    def __str__(self):
        return self.name.name
