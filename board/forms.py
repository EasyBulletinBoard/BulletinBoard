from django import forms
from .models import Board, Card
from django.contrib.auth.models import User

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name']

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'content']

class AddMemberForm(forms.Form):
    username = forms.CharField(max_length=150)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Benutzer existiert nicht.")
        return username