from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateCustomerAPIView.as_view(), name='get_customer_details'),
    path('loandetail', views.ListCreateLoanDetailAPIView.as_view(), name='get_loan_details'),
    path('emipayment', views.ListCreateEmiPaymentAPIView.as_view(), name='get_customer_details'),
]