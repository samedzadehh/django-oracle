from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="username")
    password=forms.CharField(label="password",widget=forms.PasswordInput)
    

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="username")
    password=forms.CharField(max_length=25,min_length=4,label="password",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=25,min_length=4,label="confirm",widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        
        if password and confirm and password!=confirm:
            raise forms.ValidationError("Sifreler eyni deyil(")
        values={
            "username":username,
            "password":password
        }
        return values