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
    
    def test_displaying_requests(self):
        """ test view to return correct data """
        Requests.objects.all().delete()
        Requests.objects.create(path='http://testserver/request_list/',
                req_time='2016-12-30 10:43:53',
                method='GET',
                status=200)
        for i in range(9):
            Requests.objects.create(
                path='/' + 'test' + str(i) + '/',
                req_time='2016-12-30 10:43:53',
                method='GET',
                status=200
            )
        response = self.client.get(reverse('request_list'))
        requests = Requests.objects.all().order_by('-id')[:10]
        for request in requests:
            self.assertIn(request.path, response.content)
            self.assertIn(request.method, response.content)
            self.assertIn(str(request.status), response.content)