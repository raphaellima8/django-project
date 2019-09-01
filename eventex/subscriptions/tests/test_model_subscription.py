from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.subscription = Subscription(
            name='Raphael Lima',
            email='raphael.aolima8@gmail.com',
            phone='13-991358063',
            cpf='12345678909'
        )
        self.subscription.save()


    def test_create(self):
        self.assertTrue(Subscription.objects.exists())


    def test_created_at(self):
        """Subscription must have a created_at attribute"""
        self.assertIsInstance(self.subscription.created_at, datetime)
