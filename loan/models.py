from django.db import models
from django.utils.translation import gettext_lazy as _
from django_currentuser.db.models import CurrentUserField


class Customer(models.Model):
    id = models.AutoField(primary_key=True, blank = False)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    place = models.CharField(max_length=50)


    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name

STATUS = (
    (1, _("Applied")),
    (2, _("Approved")),
    (3, _("Rejected")),
)



class LoanDetail(models.Model):
    id = models.AutoField(primary_key=True, blank = False)
    bank_user = CurrentUserField(editable=False)
    loan_description = models.CharField(max_length=50)
    amount = models.IntegerField(blank = False)
    tenure = models.IntegerField()
    loan_status = models.IntegerField(choices=STATUS, default=1, editable=False)

    def __str__(self):
        return str(self.loan_description)


EMI_STATUS = (
    (1, _("Pending")),
    (2, _("Paid")),
)
class EmiPayment(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    loan_id = models.ForeignKey(LoanDetail, on_delete=models.CASCADE)
    loan_description = models.CharField(max_length=50)
    emi_amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    status = models.IntegerField(choices=EMI_STATUS, default=1, editable=False)

    class Meta:
        verbose_name = "Loan Emi Payment"
        verbose_name_plural = "Loan Emi Payments"

    def __str__(self):
        return str(self.loan_id.loan_description)