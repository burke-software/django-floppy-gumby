from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^gumby_test/', include('floppy_gumby_forms.urls')),
)
