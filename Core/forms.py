from django import forms
from . models import ContactUs, Registration


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'contact', 'email', 'subject', 'message']

    name = forms.CharField(
        max_length=225, required=True,
        widget=forms.TextInput(
            attrs={'type': 'text',
                   'name': 'name',
                   'class': 'form-control',
                   'id': 'exampleInputName1',
                   'placeholder': 'Enter Name'
                   }
        )
    )
    contact = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'type': 'number',
                   'name': 'contact',
                   'class': 'form-control',
                   'id': 'exampleInputcontact1',
                   'placeholder': 'Enter Contact No'
                   }
        )
    )
    email = forms.EmailField(
        max_length=50, required=True,
        widget=forms.EmailInput(
            attrs={'type': 'email',
                   'name': 'email',
                   'class': 'form-control',
                   'id': 'exampleInputEmail1',
                   'placeholder': 'Enter Email'}
        )
    )
    subject = forms.CharField(
        225, required=True,
        widget=forms.TextInput(
            attrs={'type': 'text',
                   'name': 'subject',
                   'class': 'form-control',
                   'id': 'exampleInputsub1',
                   'placeholder': 'Enter Subject'}
        )
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'name': 'message',
                   'id': 'message',
                   'rows': '5'
                   }
        ),
    )


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'contact', 'student_number', 'branch',
                  'year', 'gender', 'hosteler',]

    name = forms.CharField(
        max_length=225, required=True,
        widget=forms.TextInput(
            attrs={'type': 'text',
                   'name': 'name',
                   'class': 'form-control',
                   'id': 'Name',
                   'placeholder': 'Enter Name',
                   'onblur': ''}
        )
    )
    email = forms.EmailField(
        max_length=50, required=True,
        widget=forms.EmailInput(
            attrs={'type': 'email',
                   'name': 'email',
                   'class': 'form-control',
                   'id': 'Email',
                   'placeholder': 'Enter Email'}
        )
    )
    contact = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'type': 'text',
                   'name': 'contact',
                   'class': 'form-control',
                   'id': 'Contact',
                   'placeholder': 'Enter Contact No.',
                   'onblur': ''
                   }
        )
    )
    student_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control',
                   'id': 'Student',
                   'placeholder': 'Enter Student Number',
                   'onblur': ''}
        )
    )
    BRANCH_CHOICES = [('CE', 'CE'), ('CSE', 'CSE'), ('IT', 'IT'), ('EN', 'EN'),
                      ('ECE', 'ECE'), ('EI', 'EI'), ('ME', 'ME'), ('MCA', 'MCA')]
    branch = forms.CharField(
        required=True,
        widget=forms.Select(
            choices=BRANCH_CHOICES,
            attrs={'class': 'form-control',
                   'data-val': 'true',
                   'data-val-required': '*',
                   'id': 'Branch',
                   'name': 'Branch',
                   'onchange': 'validateBranch()'})
                             )
    YEAR_CHOICES = [('2', '2'),('1', '1')]
    year = forms.CharField(
        required=True,
        widget=forms.Select(choices=YEAR_CHOICES,
                            attrs={'class': 'form-control',
                                   'data-val': 'true',
                                   'data-val-required': '*',
                                   'id': 'Year',
                                   'name': 'Year'},
                            ),
        # disabled = True,
    )
    GENDER_CHOICES = [('F', 'Female'), ('M', 'Male')]
    gender = forms.CharField(
        required=True,
        widget=forms.Select(choices=GENDER_CHOICES,
                            attrs={'class': 'form-control',
                                   'data-val': 'true',
                                   'data-val-required': '*',
                                   'id': 'Gender',
                                   'name': 'Gender',
                                   'type': 'radio'})
    )
    hosteler = forms.BooleanField(required=False,
                                  widget=forms.CheckboxInput(attrs={
                                                             'data-val': 'true',
                                                             'data-val-required': 'the hosteler field is required',
                                                             'id': 'IsHosteler',
                                                             'name': 'IsHosteler',
                                                             'type': 'checkbox'}))
    designer = forms.BooleanField(required=False,
                                  widget=forms.CheckboxInput(attrs={
                                                             'data-val': 'true',
                                                             'data-val-required': 'the designer is required',
                                                             'id': 'IsDesigner',
                                                             'name': 'IsDesigner',
                                                             'type': 'checkbox'
                                                             }))
