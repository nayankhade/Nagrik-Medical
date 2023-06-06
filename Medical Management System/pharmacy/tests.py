from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Patients, Stock, Dispense

from django.test import TestCase, Client
from django.urls import reverse
from .models import Billing

class BillingTestCase(TestCase):
    def setUp(self):
        # Create a test billing object
        Billing.objects.create(
            patient_name='Nayan Khade',
            age=21,
            mobile='7875355740',
            tablet='XYZ',
            quantity='2',
            price='3',
            total='6'
        )

    def test_billing_list_view(self):
        # Create a client and send a GET request to the billing list view
        client = Client()
        response = client.get(reverse('billing_list'))

        # Check if the response is a redirect (HTTP 302)
        self.assertEqual(response.status_code, 302)
        
        # Check if the response redirects to the correct URL
        self.assertRedirects(response, reverse('billing_create'))

    def test_billing_view(self):
        # Create a client and send a POST request to the billing view
        client = Client()
        response = client.post(reverse('billing_create'))

        # Check if the response is a redirect (HTTP 302)
        self.assertEqual(response.status_code, 302)

        # Check if a new billing object is created
        self.assertTrue(Billing.objects.filter(patient_name='Nayan Khade').exists())

        # Check if the redirect URL is correct
        self.assertRedirects(response, reverse('success'))
