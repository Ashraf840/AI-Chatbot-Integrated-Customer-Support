from django import forms
from .models import User


# User Login Form
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # to hide the password-field-value while typing

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        # NB: use this func in order to make custom-validation of each/certain field(s)
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
        return self.cleaned_data
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

class UserRegistrationForm(forms.Form):
    email = forms.CharField(max_length=30)
    username = forms.CharField(max_length=255)
    nid = forms.CharField(max_length=255)
    mobile = forms.CharField(max_length=255)
    district = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        nid = cleaned_data.get('nid')
        mobile = cleaned_data.get('mobile')
        district = cleaned_data.get('district')
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password != repeat_password:
            raise forms.ValidationError("Password does not matched!", code="PasswordMismatched")
        if not email and not username and not password and not repeat_password\
            and not mobile and not district:
            raise forms.ValidationError('You have to write something!')
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control email'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['username'].widget.attrs['class'] = 'form-control username'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['nid'].widget.attrs['class'] = 'form-control nid'
        self.fields['nid'].widget.attrs['placeholder'] = 'nid'
        self.fields['mobile'].widget.attrs['class'] = 'form-control mobile'
        self.fields['mobile'].widget.attrs['placeholder'] = 'mobile'
        self.fields['district'].widget.attrs['class'] = 'form-control district'
        self.fields['district'].widget.attrs['placeholder'] = 'district'
        self.fields['password'].widget.attrs['class'] = 'form-control password'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
        self.fields['repeat_password'].widget.attrs['class'] = 'form-control repeat_password'
        self.fields['repeat_password'].widget.attrs['placeholder'] = 'repeat_password'

class UserPasswordResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # NB: use this func in order to make custom-validation of each/certain field(s)
        # print(self.cleaned_data['password'])
        # print(self.cleaned_data['repeat_password'])
        if self.is_valid():
            password = self.cleaned_data['password']
            repeat_password = self.cleaned_data['repeat_password']
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['repeat_password'].widget.attrs['class'] = 'form-control'
        self.fields['repeat_password'].widget.attrs['placeholder'] = 'Confirm Password'
