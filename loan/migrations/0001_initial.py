# Generated by Django 3.2.13 on 2022-04-23 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='LoanDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_description', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('tenure', models.IntegerField()),
                ('loan_status', models.IntegerField(choices=[(1, 'Applied'), (2, 'Approved'), (3, 'Rejected')], default=1, editable=False)),
                ('bank_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmiPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_description', models.CharField(max_length=50)),
                ('emi_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Paid')], default=1, editable=False)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.loandetail')),
            ],
            options={
                'verbose_name': 'Loan Emi Payment',
                'verbose_name_plural': 'Loan Emi Payments',
            },
        ),
    ]
