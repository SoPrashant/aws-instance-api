from django import forms

class AccountIdForm(forms.Form):
    account_id = forms.CharField(max_length=100, required=True)
