from django.db import models

from edc_registration.models import RegisteredSubject


class SubjectDoesNotExistError(Exception):
    pass


class ValidateSybjectidentifierModelMixin(models.Model):
    """Validate subject identifier is valid against registered subject.
    The model using this mixin must have a subject identifier as a field.
    """

    def vaidate_subject_identifier(self, subject_identifier=None):
        """Check is there is a registered subject for a given subject identifier.
        """
        try:
            RegisteredSubject.objects.get(
                subject_identifier=subject_identifier)
        except RegisteredSubject.DoesNotExist:
            raise SubjectDoesNotExistError(
                f'Subject with subject identifier: {subject_identifier}'
                ' does not exist.')
