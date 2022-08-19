import os

from dal import autocomplete
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from django.utils.encoding import force_text

from .models import *


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


# class StaffForm(ModelForm): category=forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'),
# empty_label="Choose your specialization") institution=forms.ModelChoiceField(queryset=Institution.objects.all(
# ).order_by('name'), empty_label="Choose " "institute") position=forms.ModelChoiceField(
# queryset=Position.objects.all().order_by('name'), empty_label="Choose your Title") class Meta: model = Staff fields
# = ('category', 'institution', 'position')


class CourseForm(ModelForm):
    # objective = forms.CharField(widget=RichTextWidget())
    name = forms.CharField(label="Course Name", help_text="Course name must be precise, not more than 5 words",
                           required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter course name'})
                           )

    class Meta:
        model = Course
        fields = ('category', 'name', 'image', 'objective',)


class ModuleForm(ModelForm):
    title = forms.CharField(label="Module title", help_text="Module name must be precise, not more than 5 words",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'title of a topic/Module'})
                            )

    class Meta:
        model = Module
        fields = ('title', 'content')


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'sex', 'phone')


class EditCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('category', 'name', 'objective',)


class RequestForm(ModelForm):
    class Meta:
        model = TeachingRequest
        fields = ('institution', 'letter',)


# class ContentForm(ModelForm):
#     title = forms.CharField(label="Content Name", help_text="Content name must be precious, not more than 5 words",
#                             required=True,
#                             widget=forms.TextInput(attrs={'placeholder': 'Enter Content name'})
#                             )
#
#     class Meta:
#         model = Content
#         fields = ('title', 'video',)


class CourseSearchForm(ModelForm):
    class Meta:
        model = Module
        fields = ('course',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()


# class RevertForm(ModelForm):
#     reason = forms.CharField(label="Revert Reason", help_text="reason for not approved ",
#                              required=True,
#                              widget=forms.TextInput(attrs={'placeholder': 'Enter reason'})
#                              )
#
#     class Meta:
#         model = Verification
#         fields = ('reason',)


class RegisterForm(forms.ModelForm):
    """
    The default

    """

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'phone']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password is not None and password != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
