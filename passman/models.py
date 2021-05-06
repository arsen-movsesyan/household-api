from dateutil.rrule import rrule, YEARLY, MONTHLY, WEEKLY, DAILY
from django.db import models
from stdimage.models import StdImageField
from passman.managers import MailingAddressManager


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    ssn = models.CharField(max_length=9)
    dob = models.DateField()
    retired = models.BooleanField(default=False)


class Address(models.Model):
    period_start = models.DateField()
    period_end = models.DateField(null=True)
    address_id = models.CharField(max_length=255)
    formatted_address = models.CharField(max_length=255)
    apt_suite = models.CharField(max_length=255, null=True)
    comment = models.TextField(null=True)

    objects = MailingAddressManager()

    class Meta:
        ordering = ['period_start']


class Vehicle(models.Model):
    make = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    license_plate = models.CharField(max_length=255)
    vin = models.CharField(max_length=255)
    retired = models.BooleanField(default=False)
    purchase_year = models.DateField(null=True)
    retire_date = models.DateField(null=True)
    comment = models.TextField(null=True)


class PersonDocument(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='my_documents', null=True)
    document_name = models.CharField(max_length=255)
    issue_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    scan_image = StdImageField(
        variations={
            'thumbnail': (100, 70, True),
        },
        delete_orphans=True)
    is_active = models.BooleanField(default=True)
    comment = models.TextField(null=True)


class Account(models.Model):
    account_name = models.CharField(max_length=255)
    account_url = models.URLField()
    created_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    username_value = models.CharField(max_length=255)
    password_value = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_date']


class AccountExtra(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='extra_fields')
    parameter = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    comment = models.TextField(null=True)


frequency_choices = [
    (YEARLY, 'Yearly'),
    (MONTHLY, 'Monthly'),
    (WEEKLY, 'Weekly'),
    (DAILY, 'Daily')
]


class RecurringAccount(models.Model):
    account = models.OneToOneField(Account, primary_key=True, on_delete=models.DO_NOTHING)
    frequency = models.IntegerField(choices=frequency_choices, default=MONTHLY)
    extra_params = models.JSONField(null=True)
    acknowledge_required = models.BooleanField(default=True)

    def get_next_occurrence(self):
        try:
            rule = list(rrule(self.frequency, **self.extra_params))
        except TypeError as e:
            print(f'Error trying to evaluate rrule for {self.extra_params}: {e}')
            return None
        if len(rule) == 0:
            return None
        return list(rule)[0]


class RecurringAcknowledgement(models.Model):
    account = models.ForeignKey(RecurringAccount, on_delete=models.DO_NOTHING, related_name='history')
    acknowledged_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    acknowledge_value = models.CharField(max_length=255, null=True)
    comment = models.TextField(null=True)
