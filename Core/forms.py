from django import forms
from django.urls import reverse_lazy
from .models import ContactUs, Registration, Branch, Year, Gender, Event,AlumniRegistration,Domain
from django.core.validators import RegexValidator
from django.forms import ValidationError
# from snowpenguin.django.recaptcha2.fields import ReCaptchaField
# from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox
from django.core.validators import URLValidator 
from django.core.exceptions import ObjectDoesNotExist
import re
validate_url = URLValidator()
class ContactUsForm(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaWidget())
    captcha = ReCaptchaField()

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
    #captcha = ReCaptchaField(widget=ReCaptchaWidget())
    captcha = ReCaptchaField()

    class Meta:
        model = Registration
        fields = [
                    'name', 'phone','your_work','college_email',
                    'student_number','branch','year','roll_no',
                    'gender','domain','skills','hacker_rank_username', 'captcha',
                     'is_hosteler'
                ]

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

        self.fields['your_work'] = forms.CharField(
            max_length=1000,required=False,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'your_work',
                       'class': 'form-control',
                       'id': 'your_work',
                       'onblur': ''
                       }
            )
        )
        self.fields['phone'] = forms.CharField(
            required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'phone',
                       'class': 'form-control',
                       'id': 'Phone',
                       'placeholder': 'Enter Phone No.',
                       'onblur': ''
                       }
            )
        )
        self.fields['whatsapp'] = forms.CharField(
            required=False,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'whatsapp',
                       'class': 'form-control',
                       'id': 'whatsapp',
                       'placeholder': 'Enter whatsapp No.',
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
        self.fields['roll_no'] = forms.CharField(
            required=False,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'class': 'form-control',
                       'id': 'Roll_no',
                       'placeholder': 'Enter Roll Number',
                       'onblur': ''}
            )
        )
        self.fields['branch'] = forms.ModelChoiceField(
            queryset=Branch.objects.filter(active=True).order_by('name'),
            initial=Branch.objects.filter(active=True).order_by('name').first(),
            to_field_name="code",
            required=True,
            widget=forms.Select(
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'Branch',
                       'name': 'Branch',
                       }
            )
        )

        self.fields['gender'] = forms.ModelChoiceField(
            queryset=Gender.objects.all(),
            initial=Gender.objects.all().first(),
            required=True,
            widget=forms.Select(
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'gender',
                       'name': 'gender',
                       }
            )
        )
        self.fields['domain'] = forms.ModelChoiceField(
            queryset=Domain.objects.all(),
            initial=Domain.objects.all().first(),
            required=False,
            widget=forms.Select(
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'domain',
                       'name': 'domain',
                       }
            )
        )

        self.fields['skills'] = forms.CharField(
            required=False,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'skills',
                       'class': 'form-control',
                       'id': 'skills',
                       'onblur': ''
                       }
            )
        )
        self.fields['year'] = forms.ModelChoiceField(
            queryset=Year.objects.filter(active=True),
            initial=Year.objects.filter(active=True).first(),
            required=False,
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
            widget=forms.TextInput(
            attrs={
                'data-val': 'true',
                'data-val-required': '*',
                'id': 'design_tools',
                'name': 'design_tools',
                'type': 'text'
                }
            )
        )
        TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
        )
        self.fields['is_hosteler'] = forms.ChoiceField(
            choices = TRUE_FALSE_CHOICES, label="Hosteler?", 
                initial='',widget=forms.Select(
                attrs={'class': 'form-control',
                       'data-val': 'true',
                       'data-val-required': '*',
                       'id': 'Year',
                       'name': 'Year'},
            ), 
            required=True
            )
        

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        try:
            student_number = cleaned_data['student_number']
        except KeyError:
            raise ValidationError("")
        
        try:
            college_email = cleaned_data['college_email']
        except KeyError:
            raise ValidationError("")

        try:
            phone = cleaned_data['phone']
        except KeyError:
            raise ValidationError("")
            
        # try:
        #     whatsapp = cleaned_data['whatsapp']
        # except KeyError:
        #     raise ValidationError("")

        try:
            branch = cleaned_data['branch']
            branch_code = Branch.objects.get(name=branch).code
        except (KeyError, ObjectDoesNotExist):
            raise ValidationError("")

        # try:
        #     roll_no = cleaned_data['roll_no']
        # except KeyError:
        #     raise ValidationError("")


        # hacker_rank_username = cleaned_data.get('hacker_rank_username')
        # your_work = cleaned_data.get('your_work')
        # if hacker_rank_username:
        #     pattern = re.compile("^_*[a-zA-Z\\d]+[a-zA-z0-9]*$")
        #     if not pattern.match(str(hacker_rank_username)):
        #         return ValidationError("Invalid HackerRank Username")
        
        # if your_work:
        #     your_work = your_work.split(',')
        #     for link in your_work:
        #         link = link.lstrip()
        #         link = link.rstrip()

        #         if (link[:7]).lower()!='http://' and link[:8].lower()!='https://':
        #             link = 'http://'+ link
        #         try:
        #             validate_url(link)
        #         except ValidationError:
        #             raise ValidationError(f'Your work : {link} is not a valid URL')
 
        # regex_student = "^(20|21)(15|11|12|14|10|13|00|31|21|32|40)[0-9][0-9][0-9](d|D|)[-]?[mdlMDL]?";

        # registration for first year only
        regex_student = "^(21)(((11|12|14|10|13|00|31|21|32|40|153|164)[0-9][0-9][0-9])|((154|164)[0-9][0-9]))(d|D|)[-]?[mdlMDL]?$";    
        pattern_student = re.compile(regex_student)

        if student_number:
            if not pattern_student.match(str(student_number)):
                raise ValidationError("Invalid Student Number")

        # regex_college_email= "^[a-zA-Z]+(20|21)(15|11|12|14|10|13|00|31|21|32|40)[0-9][0-9][0-9](\@akgec\.ac\.in)$"

        # Check if college email contains the student number
        regex_college_email1= f"^[a-zA-Z]+({str(student_number)})(\@akgec\.ac\.in)$"
        regex_college_email2= "^[a-zA-Z]+(21)(((11|12|14|10|13|00|31|21|32|40|153|(x|X){3})[0-9][0-9][0-9])|((154)[0-9][0-9]))(\@akgec.ac.in)$"
        pattern_college_email1= re.compile(regex_college_email1)
        pattern_college_email2= re.compile(regex_college_email2)

        if college_email:
            if not pattern_college_email1.match(str(college_email)):
                if not pattern_college_email2.match(str(college_email)):
                    raise ValidationError("Invalid College Email")

        regex_phone= "^[56789]\d{9}$"
        pattern_phone=re.compile(regex_phone)

        if phone:
            if not pattern_phone.match(str(phone)):
                raise ValidationError("Invalid phone")
        # if whatsapp:
        #     if not pattern_phone.match(str(whatsapp)):
        #         raise ValidationError("Invalid Whatsapp number")
        # Check if branch code matches that of student number
        
        # Check if branch code is contained in student number
        student_number_branch_code = str(student_number)[2:5]
        pattern_branch_code = re.compile(f"^({branch_code})")
        if branch_code:
            if not pattern_branch_code.match(student_number_branch_code):   
                raise ValidationError("Student Number doesn't match that of branch code")

        # regex_roll_no = "^(21|20)00270(15|11|12|14|10|13|00|31|21|32|40)[0-9]{4}$"
        # pattern_roll_no = re.compile(regex_roll_no)

        # if not pattern_roll_no.match(str(roll_no)):
        #     raise ValidationError("Invalid Roll No. ")

        event = Event.objects.filter(active=True).first()
        if Registration.objects.filter(college_email=college_email, event=event).exists():
            raise ValidationError('Registration with this email already exist.')
        elif Registration.objects.filter(student_number=student_number, event=event).exists():
            raise ValidationError('Registration with this Student Number already exist.')
        # elif Registration.objects.filter(roll_no=roll_no, event=event).exists():
        #     raise ValidationError('Registration with this roll number already exists.')
        elif Registration.objects.filter(phone=phone, event=event).exists():
            raise ValidationError('Registration with this phone already exist.')
        # elif Registration.objects.filter(whatsapp=whatsapp, event=event).exists():
        #     raise ValidationError('Registration with this whatsapp number already exist.')


        return cleaned_data


class RegistrationAlumni(forms.ModelForm):

    phone_regex = RegexValidator(regex=r"^[56789]\d{9}$")
    contact_no = forms.CharField(validators=[phone_regex], max_length=10, required=False)
    # captcha = ReCaptchaField(widget=ReCaptchaWidget())
    captcha = ReCaptchaField()

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
