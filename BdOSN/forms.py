from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        labels = {
            "email": "Email Address",
            "password1": "Password",
            "password2": "Confirm Password",
        }
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username",
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First name",
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email address",
            }),
             "password1": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Password",
            }),
            "password2": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })


        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        # Override the username widget to include placeholder and class
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus': True,  # Django usually includes this, but good to specify
        })
        
        # Override the password widget to include placeholder and class
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })


class BookingForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Meeting Title',
            'class': 'form-control',
            'required': True
        })
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control',
            'required': True
        })
    )
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number',
            'class': 'form-control',
            'required': True
        })
    )
    date = forms.DateField(
        label='',
        widget=forms.DateInput(attrs={
            'placeholder': 'Booking date',
            'type': 'date',
            'class': 'form-control',
            'required': True
        })
    )
    start_time = forms.TimeField(
        label='',
        widget=forms.TimeInput(attrs={
            'placeholder': 'Start time',
            'type': 'time',
            'class': 'form-control',
            'required': True,
        })
    )
    end_time = forms.TimeField(
        label='',
        widget=forms.TimeInput(attrs={
            'placeholder': 'End time',
            'type': 'time',
            'class': 'form-control',
            'required': True,
        })
    )

    def __str__(self):
        return self.title
    


