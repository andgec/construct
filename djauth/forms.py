from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, UsernameField
from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _

from general.models import Company
from general.forms import CoModelForm
from djauth.models import User

UserModel = get_user_model()


class CoAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        try:
            self.company = Company.objects.get(domain=request.get_host())
            self.username_field = UserModel._meta.get_field('email')
            self.fields['username'].max_length = 254
            self.fields['username'].label = self.username_field.verbose_name.capitalize()
        except:
            self.company = None

    def clean(self):
        company = self.company
        if company:
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')

            if username is not None and password:
                users = User.objects.filter(company=company, username=username)
                user_id = users[0].id if users.count() > 0 else -1

                self.user_cache = authenticate(self.request, username=user_id, password=password)
                if self.user_cache is None:
                    raise self.get_invalid_login_error()
                else:
                    self.confirm_login_allowed(self.user_cache)

            return self.cleaned_data
        else:
            super().clean()

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': _('email [accusative]')}, #"el. pašto adresą"
        )


class CoAdminAuthenticationForm(CoAuthenticationForm, AdminAuthenticationForm):
    '''
    Custom authentication form used for admin site
    '''
    def confirm_login_allowed(self, user):
        if not user.is_staff:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': _('email [accusative]')}
            )
        super().confirm_login_allowed(user)


class CoUserCreationForm(CoModelForm, UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['unique_violation'] = _('%s with this name already exists')
        if not self.instance.id and self.request.user.is_superuser: # Superuser will create new users on "system" company to avoid duplicates
            self.co_object = 1


class CoUserChangeForm(CoModelForm, UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['unique_violation'] = _('%s with this name already exists')

    def clean(self):
        if self.request.user.is_superuser:
            self.co_object = self.data['company']
        cleaned_data = super().clean()
        return cleaned_data