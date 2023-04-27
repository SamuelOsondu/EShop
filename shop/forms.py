from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('username', css_class='wrap-input100 validate-input'),
            Field('email', css_class='wrap-input100 validate-input'),
            Field('password1', css_class='wrap-input100 validate-input'),
            Field('password2', css_class='wrap-input100 validate-input'),
            Submit('submit', 'Sign Up', css_class='wrap-login100-form-btn login100-form-btn'),
        )


class LoginForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('email', css_class='wrap-input100 validate-input'),
            Field('password', css_class='wrap-input100 validate-input'),
            Submit('submit', 'Sign Up', css_class='wrap-login100-form-btn login100-form-btn'),

        )
