from django.test import TestCase
from customers.models import Customer, Address


class TestCustomerModel(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Mobin',
            first_name='Mobin',
            last_name='aghaei',
            phone_number='09909557388',
            email='mobin@gmail.com',
            password='password'
        )

    def test_customer_is_created(self):
        self.assertEqual(str(self.customer), 'Mobinaghaei')


class TestAddressModel(TestCase):

    def setUp(self):
        customer = Customer.objects.create_user(
            username='Mobin',
            first_name='Mobin',
            last_name='aghaei',
            phone_number='09909557388',
            email='mobin@gmail.com',
            password='password'
        )

        self.address = Address.objects.create(
            customer=customer,
            address='1407 Rainbow Drive',
            country='USA',
            state='Ohio',
            city='Youngstown',
            postcode='44512'
        )

    def test_address_is_created(self):
        self.assertEqual(str(self.address), '1407 Rainbow Drive')
        self.assertEqual(self.address.address_type, 'home')
