from django.test import TestCase, Client
from apps.hello.models import Bio, Requests
from django.core.urlresolvers import reverse


class TestViewRequests(TestCase):
    def test_view_requests(self):
        """ testing request view render correctly"""
        self.client = Client()
        self.url = reverse('request_list')
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'hello/requests.html')
        self.assertEqual(response.status_code, 200)
