# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from apps.hello.models import Bio
from django.core.urlresolvers import reverse


class TestView(TestCase):
    def setUp(self):
        """creating user"""
        Bio.objects.all().delete()
        person = Bio(
            name='Andrew', last_name='Minikh',
            date_of_birth='1998-04-10', bio='Student, junior python developer',
            email='kinkrarin@gmail.com', jabber='kinkrarin@42cc.co',
            skype='kinkrarin', other_contacts='vk.com/kinkrarin')
        person.save()

    def test_profile_page(self):
        """test view with 3 db entries"""
        Bio.objects.create(name="qwerty", last_name="qwerty")
        Bio.objects.create(name="zxcv", last_name="zxcv")
        first_user = Bio.objects.first()
        self.client = Client()
        self.url = reverse('home')
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['aboutme'], first_user)
        self.assertIn('Andrew', response.content)
        self.assertIn('Minikh', response.content)
        self.assertIn('April 10, 1998', response.content)
        self.assertIn('Student, junior python developer', response.content)
        self.assertIn('kinkrarin@gmail.com', response.content)
        self.assertIn('kinkrarin@42cc.co', response.content)
        self.assertIn('kinkrarin', response.content)
        self.assertIn('vk.com/kinkrarin', response.content)

    def test_profile_page_no_entries(self):
        """test view with no entries"""
        Bio.objects.all().delete()
        self.client = Client()
        self.url = reverse('home')
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No active user is found.')

    def test_profile_page_cyrillic(self):
        """test view with cyrillic symbols"""
        Bio.objects.all().delete()
        person = Bio(
            name='Андрій', last_name='Мініх',
            bio='Студент, розробник')
        person.save()
        self.client = Client()
        self.url = reverse('home')
        response = self.client.get(self.url)
        self.assertIn('Андрій', response.content)
        self.assertIn('Мініх', response.content)
        self.assertIn('Студент, розробник', response.content)
