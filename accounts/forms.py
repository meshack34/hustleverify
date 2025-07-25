from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ServiceProviderProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ServiceProviderProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ServiceProviderProfile

SERVICE_CHOICES = [
    ('Mechanic', 'Mechanic'),
    ('Plumber', 'Plumber'),
    ('Electrician', 'Electrician'),
    ('Cleaner', 'Cleaner'),
    ('Baker', 'Baker'),
]

DAYS_OF_WEEK = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

LOCATION_CHOICES = [
    ('Nairobi', 'Nairobi'),
    ('Mombasa', 'Mombasa'),
    ('Kisumu', 'Kisumu'),
    ('Nakuru', 'Nakuru'),
    ('Eldoret', 'Eldoret'),
]

class ProviderRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    phone_number = forms.CharField(max_length=15)
    location = forms.ChoiceField(choices=LOCATION_CHOICES)
    address = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    id_number = forms.CharField(max_length=20)
    id_image = forms.ImageField(required=True, label="Upload ID Image")
    service_category = forms.ChoiceField(choices=SERVICE_CHOICES)
    availability_days = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=DAYS_OF_WEEK,
        label="Available Days"
    )
    availability_start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Availability Start Time"
    )
    availability_end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Availability End Time"
    )
    experience_years = forms.IntegerField(label="Years of Experience")
    certifications = forms.FileField(required=False, label="Upload Certifications")

    # Next of Kin fields
    next_of_kin_full_name = forms.CharField(max_length=100, label="Next of Kin Full Name")
    next_of_kin_relationship = forms.CharField(max_length=50, label="Relationship with Next of Kin")
    next_of_kin_phone = forms.CharField(max_length=15, label="Next of Kin Phone Number")


    accept_terms = forms.BooleanField(required=True, label="I accept the Terms and Conditions")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'provider'
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            ServiceProviderProfile.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                gender=self.cleaned_data['gender'],
                phone_number=self.cleaned_data['phone_number'],
                location=self.cleaned_data['location'],
                email=self.cleaned_data['email'],
                address=self.cleaned_data['address'],
                profile_picture=self.cleaned_data.get('profile_picture'),
                id_number=self.cleaned_data['id_number'],
                id_image=self.cleaned_data.get('id_image'),
                service_category=self.cleaned_data['service_category'],
                availability_days=','.join(self.cleaned_data['availability_days']),
                availability_start_time=self.cleaned_data['availability_start_time'],
                availability_end_time=self.cleaned_data['availability_end_time'],
                experience_years=self.cleaned_data['experience_years'],
                certifications=self.cleaned_data.get('certifications'),
                next_of_kin_full_name=self.cleaned_data['next_of_kin_full_name'],
                next_of_kin_relationship=self.cleaned_data['next_of_kin_relationship'],
                next_of_kin_phone=self.cleaned_data['next_of_kin_phone'],
            )
        return user

class ClientRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

