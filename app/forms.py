from django import forms
from django.utils.translation import gettext_lazy as _
from app.models import Comments, Subscribe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['content','email','name','website']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder']='Type your comments......'
        self.fields['email'].widget.attrs['placeholder']='Type your email......'
        self.fields['name'].widget.attrs['placeholder']='Type your name......'
        self.fields['website'].widget.attrs['placeholder']='Type your website......'
class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        lables={'email':_('')}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder']='Enter your Email'
class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","password1","password2")
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Enter your username'
        self.fields['email'].widget.attrs['placeholder']='Enter your Email'
        self.fields['password1'].widget.attrs['placeholder']='Enter your password'
        self.fields['password2'].widget.attrs['placeholder']='Re enter password'
    def clean_username(self):
        username=self.cleaned_data['username'].lower()
        new=User.objects.filter(username=username)
        if new.count():
           raise forms.ValidationError("user already exists")
        return username
    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        new=User.objects.filter(email=email)
        if new.count():
           raise forms.ValidationError("email already exists")
        return email
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
           raise forms.ValidationError("password doesnot match")
        return password2
