from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "text", "id": "name", "placeholder": "Enter name", "required": "required"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "id": "email",
                "pattern": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                "placeholder": "Enter email",
                "required": "required",
            }
        )
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "text", "id": "subject", "placeholder": "Subject", "required": "required"}
        )
    )
    message = forms.CharField(
        label="Write your message here:",
        widget=forms.Textarea(
            attrs={
                "id": "message",
                "class": "form-control",
                "rows": "4",
                "cols": "25",
                "required": "required",
                "placeholder": "Message",
            }
        ),
    )
