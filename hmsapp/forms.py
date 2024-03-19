# forms.py

from django import forms
from .models import staff,customer,room
class signupform(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = forms.ChoiceField(
        label='Select your gender',
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = staff
        fields = ('firstname', 'lastname', 'username', 'email', 'phone', 'gender', 'password', 'confirm_password')
        
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

        



class signupform1(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = forms.ChoiceField(
        label='Select your gender',
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = customer
        fields = ('firstname', 'lastname', 'username', 'email', 'phone', 'gender', 'password', 'confirm_password',)
        
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.TextInput(attrs={'class': 'form-control'}),
    
           
        }

        









class RoomForm(forms.ModelForm):
    class Meta:
        model = room
        fields = ('no', 'roomtype', 'price', 'availability')
        
      

        