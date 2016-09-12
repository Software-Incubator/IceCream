import os
import uuid

from django.db import models


def email_attachment_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/email_attachments', filename)


class Email(models.Model):
    sender = models.CharField(max_length=255, name='from', editable=False)
    receiver = models.EmailField(null=False, blank=False, name='to', editable=False)
    html = models.TextField(editable=False)
    sender_ip = models.GenericIPAddressField(editable=False)
    subject = models.TextField(editable=False)
    text = models.TextField(editable=False)


class Attachment(models.Model):
    email = models.ForeignKey('Email')
    file = models.FileField(upload_to=email_attachment_upload_location, null=False)
    filename = models.CharField(max_length=255, null=False, blank=False)
