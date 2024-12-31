from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        required=False,
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
    )
    subject = forms.CharField(
        max_length=200,
        required=True,
        label="Subject",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'})
    )
    message = forms.CharField(
        required=True,
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'})
    )
