from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):
  def setUp(self):
    data = dict(name='Raphael Lima', cpf='12345678909',
                email='raphael.aolima8@gmail.com', phone='13-99135-8063')
    self.resp = self.client.post('/inscricao/', data)
    self.email = mail.outbox[0]

  def test_subscription_email_subject(self):
    expect = 'Confirmação de inscrição'
    self.assertEqual(expect, self.email.subject)
  
  def test_subscription_email_from(self):
    expect = 'contato@eventex.com.br'
    self.assertEqual(expect, self.email.from_email)
    
  def test_subscription_email_to(self):
    expect = ['contato@eventex.com.br', 'raphael.aolima8@gmail.com']
    
    self.assertListEqual(expect, self.email.to)
  
  def test_subscription_email_body(self):
    contents = ('Raphael Lima',
               '12345678909',
               'raphael.aolima8@gmail.com',
               '13-99135-8063')
    for content in contents:
        with self.subTest():
            self.assertIn(content, self.email.body)
