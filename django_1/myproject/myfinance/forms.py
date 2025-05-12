from django import forms
from django import models
from .models import Member
from .models import Account

class Member(models.Member):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Account(models.Account):
    title = models.CharField(max_length=100)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return self.title

class MemberForm(forms.MemberForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'member_id']

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if "bad" in title.lower():
                raise forms.ValidationError("Inappropriate word detected in title.")
            return title
        
from django import forms
from .models import Member

class AccountForm(forms.AccountForm):
    class Meta:
        model = Account
        fields = ['accounttype', 'amountinacc', 'ROI']

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if "bad" in title.lower():
                raise forms.ValidationError("Inappropriate word detected in title.")
            return title