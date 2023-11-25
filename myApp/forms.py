from django import forms
from .models import Complaint


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


 