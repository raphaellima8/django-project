from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionTest(TestCase):
  def setUp(self):
    self.resp = self.client.get('/inscricao/')
  def test_get(self):
    """Must return status code 200"""
    self.assertEqual(200, self.resp.status_code)
  
  def test_template(self):
    """Must use subscriptions/subscription_form.html"""
    self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
  
  def test_input(self):
    self.assertContains(self.resp, '<form')
    self.assertContains(self.resp, '<input', 6)
    self.assertContains(self.resp, 'type="text"', 3)
    self.assertContains(self.resp, 'type="email"')
    self.assertContains(self.resp, 'type="submit"')
  
  def test_csrf(self):
    self.assertContains(self.resp, 'csrfmiddlewaretoken')
    
  def test_has_form(self):
    form = self.resp.context['form']
    self.assertIsInstance(form, SubscriptionForm)
  
  def test_has_fields(self):
    form = self.resp.context['form']
    self.assertSequenceEqual(['name', 'email', 'cpf', 'phone'], list(form.fields))