from django import forms
from contact.models import Contact


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

    def clean(self):
        has_errors = False
        if len(self.cleaned_data["name"]) > 30:
            self.add_error("name", "Name is too long: max 30")
            has_errors = True
        if "@" not in self.cleaned_data["email"]:
            self.add_error("message", "Email is not valid")
            has_errors = True
        if len(self.cleaned_data["subject"]) > 50:
            self.add_error("subject", "Subject is too long: max 50")
            has_errors = True
        if len(self.cleaned_data["message"]) > 500:
            self.add_error("message", "Message is too long: max 500")
            has_errors = True

        if has_errors:
            print("Invalid")
            raise forms.ValidationError("Invalid data")
        return self.cleaned_data

    def save(self):
        Contact.objects.create(**self.cleaned_data)
