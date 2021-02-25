from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super(UserProfileForm, self).__init__(*args, **kwargs)

        placeholders = {
            'display_name': 'Display Name',
            'phone': 'Phone Number',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'city': 'City or Town',
            'postcode': 'Postal Code',
            'county': 'County or State',
            'country': 'Country',
        }

        self.fields['phone'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'country' and field != 'avatar':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'text-input-field mb-3'
                self.fields[field].label = False