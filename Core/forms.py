from django import forms
from django.urls import reverse_lazy
from .models import ContactUs, Registration, Branch, Year, Gender, Event,AlumniRegistration,Domain
from django.core.validators import RegexValidator
from django.forms import ValidationError
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from django.core.validators import URLValidator 
import datetime
import re
validate_url = URLValidator()
class ContactUsForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = ContactUs
        fields = ['name', 'contact', 'email', 'subject', 'message','captcha']

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
        max_length=225, required=True,
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
    # captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = Registration
        fields = ['name', 'contact','whatsapp_no','college_email', 'student_number','branch','year',
                    'account_handles','experience','about_yourself','why_attend',
                        'design_tools','insta_improvement']#,'captcha']
        exclude = ['event']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(
            max_length=80, required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'name',
                       'class': 'form-control',
                       'id': 'Name',
                       'placeholder': 'Enter Name',
                       'onblur': ''}
            )
        )
        self.fields['college_email'] = forms.EmailField(
            max_length=50, required=True,
            widget=forms.EmailInput(
                attrs={'type': 'email',
                       'class': 'form-control',
                       'id': 'Email',
                       'placeholder': 'Enter AKGEC provided Email',
                       'onblur': ''}
            )
        )
        self.fields['account_handles'] = forms.CharField(
            max_length=500,required=False,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'account_handles',
                       'class': 'form-control',
                       'id': 'account_handles',
                       'onblur': ''
                       }
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
        self.fields['whatsapp_no'] = forms.CharField(
            required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'class': 'form-control',
                       'id': 'Whatsapp',
                       'placeholder': 'Enter Whatsapp No.',
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
            queryset=Branch.objects.filter(active=True).order_by('name'),
            initial=Branch.objects.filter(active=True).order_by('name').first(),
            required=True,
            widget=forms.Select(
                # choices=BRANCH_CHOICES,
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'Branch',
                       'name': 'Branch',
                       }
            )
        )
        self.fields['experience'] = forms.ChoiceField(
            choices=Registration.experience_choices,
            label = 'Experience',
            required=True,
            widget=forms.Select(
                # choices=BRANCH_CHOICES,
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'Experience',
                       'name': 'Experience',
                       }
            )
        )
        self.fields['insta_improvement'] = forms.CharField(
            required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'insta_improvement',
                       'class': 'form-control',
                       'id': 'insta_improvement',
                       'onblur': ''
                       }
            )
        )
        self.fields['about_yourself'] = forms.CharField(
            required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'about_yourself',
                       'class': 'form-control',
                       'id': 'about_yourself',
                       'onblur': ''
                       }
            )
        )
        # self.fields['domain'] = forms.ModelChoiceField(
        #     queryset=Domain.objects.all(),
        #     required=True,
        #     widget=forms.Select(
        #         attrs={'class': 'form-control',
        #                'data-val': 'true',
        #                'data-val-required': '*',
        #                'id': 'Domain',
        #                'name': 'Domain',
        #                'type': 'radio'}
            
        #     )
        # )
        self.fields['year'] = forms.ModelChoiceField(
            queryset=Year.objects.filter(active=True),
            initial=Year.objects.filter(active=True).first(),
            required=True,
            widget=forms.Select(
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'Year',
                       'name': 'Year'},
            ),
        )
        self.fields['design_tools'] = forms.CharField(
            required=False,
            initial="",
            label = "Names of designing tools you are familiar with(if any)?",
            widget=forms.CheckboxInput(
            attrs={
                'data-val': 'true',
                'data-val-required': '*',
                'id': 'design_tools',
                'name': 'design_tools',
                'type': 'text'
                }
            )
        )
        # self.fields['gender'] = forms.ModelChoiceField(
        #     queryset=Gender.objects.all(),
        #     required=True,
        #     widget=forms.Select(
        #         attrs={'class': 'form-control',
        #                'data-val': 'true',
        #                'data-val-required': '*',
        #                'id': 'Gender',
        #                'name': 'Gender',
        #                'type': 'radio'})
        # )
        # self.fields['github_username'] = forms.CharField(
        #     required=True,
        #     widget=forms.TextInput(
        #         attrs={'type': 'text',
        #                'class': 'form-control',
        #                'id': 'github_username',
        #                'name': 'github_username',
        #                'placeholder': 'Enter github username'
        #                })
        # )
        # self.fields['hosteler'] = forms.BooleanField(
        #     required=False,
        #     widget=forms.CheckboxInput(
        #     attrs={
        #         'data-val': 'true',
        #         'data-val-required': 'the hosteler field is required',
        #         'id': 'IsHosteler',
        #         'name': 'IsHosteler',
        #         'type': 'checkbox'}
        #     )
        # )
        # self.fields['skills'] = forms.CharField(
        #     max_length=500,required=False,
        #     widget=forms.TextInput(
        #         attrs={'type': 'text',
        #                'name': 'skills',
        #                'class': 'form-control',
        #                'id': 'Skills',
        #                'onblur': ''
        #                }
        #     )
        # )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        # university_roll_no = None
        # team_name = None
        # codechef_name = None

        try:
            student_number = cleaned_data['student_number']
        except KeyError:
            raise ValidationError("")
        
        try:
            college_email = cleaned_data['college_email']
        except KeyError:
            raise ValidationError("")

        try:
            contact = cleaned_data['contact']
        except KeyError:
            raise ValidationError("")

        try:
            whatsapp_no = cleaned_data['whatsapp_no']
        except KeyError:
            raise ValidationError("")
        account_handles = cleaned_data.get('account_handles',None)

        if account_handles:
            account_handles = account_handles.split(',')
            for ah in account_handles:
                ah = ah.lstrip()
                ah = ah.rstrip()
                try:
                    validate_url(ah)
                except:
                    raise ValidationError(f'Handles : {ah} is not a valid URL')

        # try:
        #     university_roll_no = cleaned_data['university_rollno']
        # except KeyError:
        #     raise ValidationError("")

        # try:
        #     team_name = cleaned_data['codechef_team_name']
        # except KeyError:
        #     raise ValidationError("")

        # try:
        #     codechef_name = cleaned_data['codechef_handle']
        # except KeyError:
        #     raise ValidationError("")

        year = datetime.date.today().year-1
        end = ''
        start = ''

        for i in range(year, year-4, -1):
            end += str(i % 10)
            i = int(i/10)
            start += str(i % 10)

        # start=1111 , end=9876    
        regex_student = "^(17|18|19|20)(11|12|14|10|13|00|31|21|32|40)[0-2][0-9][0-9]$";    
        #regex_student = "^["+start+"]["+end+"](11|12|14|10|13|00|31|21|32|40)[0-2][0-9][0-9][-]?[mdlMDL]?$"
        # regex_university = "^["+start+"]["+end+"][0][2][7](12|14|10|13|00|31|21|32|40)[0-9][0-9][0-9]$"
        pattern_student = re.compile(regex_student)
        # pattern_university = re.compile(regex_university)

        if student_number:
            if not pattern_student.match(str(student_number)):
                raise ValidationError("Invalid Student Number")

        # regex_github = "^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$"
        # pattern_github = re.compile(regex_github)

        # if github_username:
        #     if not pattern_github.match(str(github_username)):
        #         raise ValidationError("Invalid Github Username")

        regex_college_email= "^[a-zA-Z]+(18|19)(11|12|14|10|13|00|31|21|32|40)[0-2][0-9][0-9](\@akgec\.ac\.in)$"
        pattern_college_email= re.compile(regex_college_email)

        if college_email:
            if not pattern_college_email.match(str(college_email)):
                raise ValidationError("Invalid College Email")

        regex_contact= "^[56789]\d{9}$"
        pattern_contact=re.compile(regex_contact)

        if contact:
            if not pattern_contact.match(str(contact)):
                raise ValidationError("Invalid contact")

        regex_whatsapp_no= "^[56789]\d{9}$"
        pattern_whatsapp_no=re.compile(regex_whatsapp_no)

        if whatsapp_no:
            if not pattern_contact.match(str(whatsapp_no)):
                raise ValidationError("Invalid whatsapp_no")

        # if university_roll_no:
        #     if not pattern_university.match(str(university_roll_no)):
        #         raise ValidationError("Invalid University Roll Number")


        event = Event.objects.filter(active=True).first()

        if Registration.objects.filter(college_email=college_email, event=event, student_number=student_number).exists():
            raise ValidationError('Registration with this student number and email already exist.')
        elif Registration.objects.filter(student_number=student_number, event=event).exists():
            raise ValidationError('Registration with this student number already exist.')
        elif Registration.objects.filter(college_email=college_email, event=event).exists():
            raise ValidationError('Registration with this email already exist.')
        elif Registration.objects.filter(contact=contact, event=event).exists():
            raise ValidationError('Registration with this contact already exist.')
        elif Registration.objects.filter(whatsapp_no=whatsapp_no, event=event).exists():
            raise ValidationError('Registration with this whatsapp no. already exist.')


        # if team_name:
        #     if Registration.objects.filter(codechef_team_name=team_name).exists():
        #         raise ValidationError("Team cannot have more than two members")

        # if codechef_name:
        #     if Registration.objects.filter(codechef_handle=codechef_name).exists():
        #         raise ValidationError("Already registered handle")

        return cleaned_data


class RegistrationAlumni(forms.ModelForm):

    phone_regex = RegexValidator(regex=r"^[56789]\d{9}$")
    contact_no = forms.CharField(validators=[phone_regex], max_length=10, required=False)
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = AlumniRegistration
        fields = ['name', 'batch', 'contact_no', 'message','date','captcha']


    def __init__(self, *args, **kwargs):
        super(RegistrationAlumni, self).__init__(*args, **kwargs)

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
        self.fields['contact_no'] = forms.CharField(
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
