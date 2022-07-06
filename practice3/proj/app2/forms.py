from django import forms
class registerform(forms.Form):
    username=forms.CharField(max_length=100)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)