from django import forms
from .models import CustomShieldOrder

class CustomShieldOrderForm(forms.ModelForm):
    class Meta:
        model = CustomShieldOrder
        fields = ('lord_name', 'shield_type', 'heraldry_description')
        widgets = {
            'lord_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Lord's Title & Name (e.g., Sir Richard)"
            }),
            'shield_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'heraldry_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe your order specifications...',
                'style': 'resize: vertical;'
            }),
        }