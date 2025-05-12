from django import forms
from .models import Member


class MemberForm(forms.MemberForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'member_id']

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if "bad" in title.lower():
                raise forms.ValidationError("Inappropriate word detected in title.")
            return title