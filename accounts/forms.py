from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, authenticate
from django.forms import ModelForm

from accounts.models import Profile



User = get_user_model()

class GuestForm(forms.Form):
	email = forms.EmailField()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput( attrs={"class": "form-control", "placeholder": "Username"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Password"}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Wrong username or password")


class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput( attrs={"class": "form-control", "placeholder": "Username"}))
	email    = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder": "Your email Address"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Confirm Password"}))
	


	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		return email
    
	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords must match.")
		return data


class UserForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput( attrs={"class": "form-control", "placeholder": "First Name"}))
	last_name    = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Last Name"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder": "name@example.com"}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
	image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": "form-control-file", "placeholder": "First Name"}))
	other_name    = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Other Name"}))
	birth_date = forms.DateField(input_formats=['%d/%m/%Y'],widget=forms.DateInput(attrs={"class": "form-control datetimepicker-input","placeholder": 'dd/mm/yyyy Eg. 24/05/1990'}))
	bio    = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Biography"}))
	phone = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control","placeholder": "Phone"}))
	class Meta:
		model = Profile
		fields = [
		'image',
		'other_name',
		'birth_date',
		'district',
		'bio',
		'phone'
		]









