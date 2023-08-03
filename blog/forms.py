from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "image", "text", "author", "short_desc", "tags")
        widgets = {"author": forms.HiddenInput(), "short_desc": forms.HiddenInput()}

    def clean(self):
        self.cleaned_data["short_desc"] = self.cleaned_data["text"][:15] + " ..."
        return self.cleaned_data
