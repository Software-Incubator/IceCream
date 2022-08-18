import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value)[1]
    if ext.lower() != '.pdf':
        raise ValidationError(u'File extension should be pdf!')
    
