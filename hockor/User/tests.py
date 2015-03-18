"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
     def test_login(self):
     	response = self.client.get('/login')
     	self.failUnlessEqual('',response.content)

     def test_register(self):
     	response = self.client.get('/register')
     	self.failUnlessEqual('',response.content)
     
     def test_logout(self):
     	response = self.client.get('/logout')
     	self.failUnlessEqual('',response.content)
