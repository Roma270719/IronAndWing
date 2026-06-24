from django import forms
from .models import BattleReview

class CaravanOrderForm(forms.Form):
    PACE_CHOICES = [
        ('SLOW', '🐂 Oxen Caravan (Safe & Slow - 3 days)'),
        ('FAST', '🐎 Swift War-Horses (Express - 1 day) (+100 Gold)'),
    ]

    NOTIFY_CHOICES = [
        ('PIGEON', '🐦 Carrier Pigeon (Standard Notification)'),
        ('RAVEN', '🦅 Dark Raven (Priority Alert)'),
    ]

    castle_address = forms.CharField(
        label="Destination Castle / Faction",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-dark text-white border-secondary',
            'placeholder': 'Enter your stronghold name...',
        }),
    )

    delivery_pace = forms.ChoiceField(
        label="Caravan Pace",
        choices=PACE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control bg-dark text-white border-secondary'
        })
    )

    notification_method = forms.ChoiceField(
        label="Arrival Notification",
        choices=NOTIFY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control bg-dark text-white border-secondary'
        })
    )


class BattleReviewForm(forms.ModelForm):
    class Meta:
        model = BattleReview
        fields = ['review', 'rating']
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control',
                                            'rows': 4, 'placeholder': 'Your Review...'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control',
                                               'type': 'number', 'min': 1, 'max': 5}),
        }