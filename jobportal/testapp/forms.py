from django import forms
from django.core import validators
def start_with(value):
       if value[0] !='d':
           raise forms.ValidationError("start with d")
def char_fieldoption(value):
       if value.isalpha() != True:
           raise forms.ValidationError("not alphabet")
class FeedBackForm(forms.Form):
       name=forms.CharField(validators=[start_with,char_fieldoption])
       email=forms.EmailField()
       password=forms.CharField(widget=forms.PasswordInput)
       rpassword=forms.CharField(label='password(Again)',widget=forms.PasswordInput)
       message=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])
       bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

       def clean(self):
          print("bot validation")
          cleaned_data=super().clean()
          bot_handler_value=cleaned_data["bot_handler"]
          if(len(bot_handler_value) >0):
              raise forms.ValidationError("we cannot process the form,we found some issue")
          inputpassword=cleaned_data["password"]
          inputrpassword=cleaned_data["rpassword"]
          if inputpassword!=inputrpassword:
              raise forms.ValidationError("password doesnt match")
