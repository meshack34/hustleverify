# # services/forms.py
# from django import forms
# from services.models import Service, City, Location

# class ServiceFilterForm(forms.Form):
#     service_type = forms.ChoiceField(
#         choices=Service._meta.get_field('service_type').choices,
#         label="Select Service Type",
#         required=True
#     )
#     city = forms.ModelChoiceField(
#         queryset=City.objects.all(),
#         label="Select City",
#         required=True
#     )
#     location = forms.ModelChoiceField(
#         queryset=Location.objects.none(),
#         label="Select Location",
#         required=False
#     )

#     def __init__(self, *args, **kwargs):
#         super(ServiceFilterForm, self).__init__(*args, **kwargs)
#         if 'city' in self.data:
#             try:
#                 city_id = int(self.data.get('city'))
#                 self.fields['location'].queryset = Location.objects.filter(city_id=city_id)
#             except (ValueError, TypeError):
#                 pass
#         elif self.initial.get('city'):
#             self.fields['location'].queryset = Location.objects.filter(city=self.initial['city'])



# services/forms.py
# from django import forms
# from services.models import Service, City, Location

# class ServiceFilterForm(forms.Form):
#     service_type = forms.ChoiceField(
#         choices=Service._meta.get_field('service_type').choices,
#         label="Select Service Type",
#         required=True
#     )
#     city = forms.ModelChoiceField(
#         queryset=City.objects.all(),
#         label="Select City",
#         required=True
#     )
#     location = forms.ModelChoiceField(
#         queryset=Location.objects.none(),
#         label="Select Location",
#         required=False
#     )

#     def __init__(self, *args, **kwargs):
#         super(ServiceFilterForm, self).__init__(*args, **kwargs)
#         if 'city' in self.data:
#             try:
#                 city_id = int(self.data.get('city'))
#                 self.fields['location'].queryset = Location.objects.filter(city_id=city_id)
#             except (ValueError, TypeError):
#                 pass
#         elif self.initial.get('city'):
#             self.fields['location'].queryset = Location.objects.filter(city=self.initial['city'])


# services/forms.py
from django import forms
from django import forms

SERVICE_CHOICES = [
    ('Mechanic', 'Mechanic'),
    ('Plumber', 'Plumber'),
    ('Electrician', 'Electrician'),
    ('Cleaner', 'Cleaner'),
    ('Baker', 'Baker'),
    ('Gardener', 'Gardener'),
    ('Painter', 'Painter'),
    ('Carpenter', 'Carpenter'),
    ('Tailor', 'Tailor'),
    ('Mamafua', 'Mamafua'),   
    ('Mason', 'Mason'),
    ('Chef', 'Chef'),
    ('Hairdresser', 'Hairdresser'),
    ('Photographer', 'Photographer'),
    ('Tutor', 'Tutor'),
    ('Home Repairs & Maintenance', 'Home Repairs & Maintenance'),
    
]

class ServiceFilterForm(forms.Form):
    service_category = forms.ChoiceField(choices=[('', 'Select a Service')] + SERVICE_CHOICES, required=False, label="Find Service")
