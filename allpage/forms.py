from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='이메일')
    subject = forms.CharField(required=True, label='제목')
    message = forms.CharField(widget=forms.Textarea, required=True, label='내용')