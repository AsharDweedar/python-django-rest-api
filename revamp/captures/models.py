# from django.db import models

# # Create your models here.
from mongoengine import Document, EmbeddedDocument, fields


# class CaptureInput(EmbeddedDocument):
#     name = fields.StringField(required=True)
#     value = fields.DynamicField(required=True)


class Captures(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    # inputs = fields.ListField(fields.EmbeddedDocumentField(CaptureInput))
    def __unicode__(self):
            return self.title
