from django import forms

from accounts.models import UserProfile
from django.contrib.auth import get_user_model


class UserProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birthday'].help_text = 'YYYY-MM-DD'
        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = UserProfile
        fields = (
            'gender', 'orientation', 'birthday', 'location', 'about', 'avatar', 'partner_age',
            'partner_gender', 'partner_orientation')
        required = ('gender', 'orientation', 'birthday', 'location', 'about', 'partner_age',
            'partner_gender', 'partner_orientation')


class UserEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')
        required = ('first_name', 'last_name')


