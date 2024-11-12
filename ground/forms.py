from django import forms

class StudentLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        error_messages={'invalid': 'Please enter a valid email address.'}
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        error_messages={'required': 'Password is required.'}
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password

class TeacherLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        error_messages={'invalid': 'Please enter a valid email address.'}
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        error_messages={'required': 'Password is required.'}
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password



