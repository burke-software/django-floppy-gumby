from django.test import TestCase
from django.core.urlresolvers import reverse

class SimpleTest(TestCase):
    def test_render_forms(self):
        """ Render gumby style form 
        Just check to make sure the form renders as expected
        """
        response = self.client.get(reverse('gumby_test'))
        self.assertContains(response, '<input class=" input " type="text" name="name" required id="id_name">')
