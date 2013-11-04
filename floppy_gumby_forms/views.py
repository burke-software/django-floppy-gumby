import floppyforms as forms
from django.views.generic.edit import FormView


class ContactForm(forms.Form):
    name = forms.CharField()


class GumbyTestView(FormView):
    template_name = 'gumby_test.html'
    form_class = ContactForm
