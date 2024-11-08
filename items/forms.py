from django import forms


class ItemShareForm(forms.Form):
    name = forms.CharField(max_length=64, label='Your name')
    email = forms.EmailField(label='Your email')
    to = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea, required=False)
