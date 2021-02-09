from django.contrib.sites.shortcuts import get_current_site
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAllauthAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        current_site = get_current_site(request)
        return '{}/confirm-email/?key={}'.format(current_site, emailconfirmation.key)

    def save_user(self, request, user, form, commit=True):
        user = super(CustomAllauthAdapter, self).save_user(request, user, form, commit=False)
        email = form.cleaned_data.get('email')
        ku = email.split('@', 1)[1]
        if(ku != 'st.kyoto-u.ac.jp'):
            return
        user.save()
