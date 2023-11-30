from django import forms
from .models import Complaint, MissingPerson


class ComplaintForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Complaint.CATEGORY_CHOICES, required=True,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'age', 'gender', 'phone', 'place','category', 'description']
       
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }  
class MissingPersonForm(forms.ModelForm):
    class Meta:
        model = MissingPerson
        fields = ['name', 'missing_person_name', 'missing_person_description', 'age', 'gender', 'contact_number', 'missing_person_photo']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
            'missing_person_name': forms.TextInput(attrs={'placeholder': 'Enter Missing Person\'s Name'}),
            'missing_person_description': forms.Textarea(attrs={'placeholder': 'Enter the details of the missing person...'}),
            'age': forms.TextInput(attrs={'placeholder': 'Enter Missing Person\'s Age'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter Your Contact Number'}),
        }


 