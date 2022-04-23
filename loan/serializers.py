from rest_framework import serializers
from .models import Customer,LoanDetail,EmiPayment
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):  # create class to serializer model
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Customer
        fields = ('customer_id', 'name', 'age', 'gender', 'place','owner')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model

    class Meta:
        model = User
        fields = ('id', 'username', 'customers')

class LoanDetailSerializer(serializers.ModelSerializer):  # create class to serializer model
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LoanDetail
        fields = ('loan_number', 'money_required', 'expected_percentage', 'expected_emi_tenure', 'loan_reason',
                  'loan_status', 'customer','owner')

class EmiPaymentSerializer(serializers.ModelSerializer):  # create class to serializer model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = EmiPayment
        fields = ('emi_amount', 'allocated_percentage', 'allocated_emi_tenure', 'loan_detail','owner')