from django.test import TestCase
from .admin import LoanDetail

class LoanDetailModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        LoanDetail.objects.create(loan_description='Personal Loan', amount=100, tenure=2)

    def test_first_name_label(self):
        loan_detail = LoanDetail.objects.get(id=1)
        field_label = loan_detail._meta.get_field('loan_description').verbose_name
        self.assertEqual(field_label, 'loan description')
