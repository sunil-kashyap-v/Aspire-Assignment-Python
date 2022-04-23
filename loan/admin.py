from django.contrib import admin
from .models import LoanDetail,EmiPayment
from datetime import datetime, timedelta


class LoanDetailAdmin(admin.ModelAdmin):
    list_display = ("loan_description", "amount", "tenure", "loan_status")

    def save_model(self, request, obj, form, change):
        if str(request.user) == 'admin' and obj.loan_status == 1:
            obj.loan_status = 2
            obj.save()

            cnt = 1
            for i in range(int(obj.tenure)):

                today = datetime.now() + timedelta(7*cnt)

                emi_obj = EmiPayment()
                emi_obj.emi_amount = obj.amount / obj.tenure
                emi_obj.date = today
                emi_obj.loan_description = obj.loan_description
                emi_obj.loan_id = obj
                emi_obj.save()
                cnt +=1

        super(LoanDetailAdmin, self).save_model(request, obj, form, change)

admin.site.register(LoanDetail,LoanDetailAdmin)

class EmiPaymentAdmin(admin.ModelAdmin):
    list_display = ("loan_description", "emi_amount", "date", "status")

    def save_model(self, request, obj, form, change):
        # date check
        if obj.status == 1:
            obj.status = 2
            obj.save()

admin.site.register(EmiPayment,EmiPaymentAdmin)