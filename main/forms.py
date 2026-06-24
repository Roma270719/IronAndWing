from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name',
                                           'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Email',
                                             'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Your message or question to the Guild blacksmiths...',
                                             'rows': 5,
                                             'style': 'border-radius: 5px; padding: 10px; margin-bottom: 15px;',
                                             'required': True}),
        }