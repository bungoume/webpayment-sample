from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^', include('webfront.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^payments/', include('payments.urls')),
    url(r'^accounts/', include('account.urls')),
)
