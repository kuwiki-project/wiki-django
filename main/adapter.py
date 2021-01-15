from django.contrib.sites.shortcuts import get_current_site
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class CustomAllauthAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        current_site = get_current_site(request)
        return '{}/confirm-email/?{}'.format(current_site, emailconfirmation.key)