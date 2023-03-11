from accounts.models import CustomUser
from django.db import models

class Balancesheet(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='User',on_delete=models.PROTECT)
    category = models.CharField(verbose_name='Category',max_length=10)
    amount = models.PositiveIntegerField(verbose_name='Amount')
    date = models.DateField(verbose_name='date',auto_now_add=True)

    class Meta:
        verbose_name_plural='Balancesheet'

    def __str__(self):
        return self.date