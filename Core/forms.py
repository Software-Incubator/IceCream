from django import forms

from .models import ContactUs, Registration, Branch, Year, Gender, Event

from django.forms import ValidationError



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
        exclude = ['event', 'fee_paid']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(
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

        self.fields['email'] = forms.EmailField(
            max_length=50, required=True,
            widget=forms.EmailInput(
                attrs={'type': 'email',
                       'name': 'email',
                       'class': 'form-control',
                       'id': 'Email',
                       'placeholder': 'Enter Email'}
            )
        )

        self.fields['contact'] = forms.CharField(
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
        self.fields['student_number'] = forms.CharField(
            required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'class': 'form-control',
                       'id': 'Student',
                       'placeholder': 'Enter Student Number',
                       'onblur': ''}
            )
        )

        self.fields['branch'] = forms.ModelChoiceField(
            queryset=Branch.objects.filter(active=True),
            required=True,
            widget=forms.Select(
                # choices=BRANCH_CHOICES,
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'Branch',
                       'name': 'Branch',
                       'onchange': 'validateBranch()'}
            )
        )

        self.fields['year'] = forms.ModelChoiceField(
            queryset=Year.objects.filter(active=True),
            required=True,
            widget=forms.Select(
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'Year',
                       'name': 'Year'},
            ),
        )

        self.fields['gender'] = forms.ModelChoiceField(
            queryset=Gender.objects.all(),
            required=True,
            widget=forms.Select(
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'Gender',
                       'name': 'Gender',
                       'type': 'radio'})
        )

        self.fields['hosteler'] = forms.BooleanField(
            required=False,
            widget=forms.CheckboxInput(
            attrs={
                'data-val': 'true',
                'data-val-required': 'the hosteler field is required',
                'id': 'IsHosteler',
                'name': 'IsHosteler',
                'type': 'checkbox'}
            )
        )

    def clean(self):
        registered = None
        email_exist = None
        student_number = self.cleaned_data['student_number']
        email = self.cleaned_data['email']
        student_number = int(student_number)
        event = Event.objects.filter(active=True).first()
        try:
            registered = Registration.objects.filter(student_number=student_number, event=event)
        except:
            return student_number

        try:
            email_exist = Registration.objects.filter(email=email, event=event)
        except:
            return email

        if registered and email_exist:
            raise ValidationError("Student number and email already Registered")
        elif registered:
            raise ValidationError("Student number already Registered")
        elif email_exist:
            raise ValidationError("Email already Registered")
