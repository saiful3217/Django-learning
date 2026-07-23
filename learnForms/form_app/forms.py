from django import forms
from django.core import validators
class contactForm(forms.Form):
    name= forms.CharField(label='User Name', initial='Rahim', help_text='must be valid name',required=False,widget=forms.Textarea)
    # file=forms.FileField()
    email = forms.EmailField(label='User Email')
    age= forms.IntegerField()
    weight=forms.FloatField
    balance= forms.DecimalField()
    check= forms.BooleanField()
    birthday= forms.DateField(widget=forms.DateInput(attrs={'type':'Date'}))
    appinment=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOICES=[('S','small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL=[('P','Peparoni'),('M','Mashroom'),('B','Beef')]
    pizza=forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name= forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname= self.cleaned_data['name']
    #     if len(valname) > 10 :
    #         raise forms.ValidationError(message='enter a name less than 10')
    #     return valname
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if 'h' not in valemail or '.com' not in valemail:
    #         raise forms.ValidationError(message='c or .commissing')
    #     return valemail

    # def clean(self):
    #         self.clean_data=super().clean()

    #         valname=self.clean_data['name']
    #         if len(valname) <10 :
    #             raise forms.ValidationError(message='too short name ')


class StudentData(forms.Form):
    name= forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(10,message='can submit at max 10 character'),validators.MinLengthValidator(3,message='at least 3 haracter needed ')])
    email=forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='input valid email')])
    age=forms.IntegerField(widget=forms.NumberInput, validators=[validators.MinValueValidator(45), validators.MaxValueValidator(99)])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='jpg not allowed')])
    def text_len(txt):
        if len(txt)<7:
            raise forms.ValidationError(message='very short txt')
    text=forms.CharField(validators=[text_len])

class PasswordValidationProject(forms.Form):
    name= forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput )
    def clean(self):
        clean_data= super().clean()
        valpass=clean_data['password']
        valrepass=clean_data['repassword']
        if valpass != valrepass:
            raise forms.ValidationError(message='password didnt match')
