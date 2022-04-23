
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django_filters import rest_framework as filters
from .models import Customer, LoanDetail, EmiPayment
from .serializers import CustomerSerializer, LoanDetailSerializer, EmiPaymentSerializer


class ListCreateCustomerAPIView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(owner=self.request.user)

class RetrieveUpdateDestroyCustomerAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ListCreateLoanDetailAPIView(ListCreateAPIView):
    serializer_class = LoanDetailSerializer
    queryset = LoanDetail.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveUpdateDestroyLoanDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LoanDetailSerializer
    queryset = LoanDetail.objects.all()


class ListCreateEmiPaymentAPIView(ListCreateAPIView):
    serializer_class = EmiPaymentSerializer
    queryset = EmiPayment.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(owner=self.request.user)

class RetrieveUpdateDestroyEmiPaymentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmiPaymentSerializer
    queryset = EmiPayment.objects.all()
