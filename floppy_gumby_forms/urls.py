# This is just for testing and demostration. Don't include it.
from django.conf.urls.defaults import *
from .views import *


urlpatterns = patterns('',
    url('^gumby_form_test/$', GumbyTestView.as_view(), name='gumby_test'),
)
