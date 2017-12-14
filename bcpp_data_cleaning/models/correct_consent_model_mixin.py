from edc_registration.models import RegisteredSubject
from django.core.exceptions import ValidationError


class CorrectConsentValueMisMatchError(Exception):
    pass


class CorrectConsentMixin:

    """A model linked to the subject consent to record corrections."""

    def compare_old_value_to_new_value(self, subject_identifier=None):
        """Raises an exception if an 'old_" field matchs the new value
        or both old and new are not provided."""
        for field in self._meta.fields:
            if field.name.startswith('old_'):
                old_value = getattr(self, field.name)
                new_value = getattr(
                    self, 'new_{}'.format(field.name.split('old_')[1]))
                if (not old_value and new_value) or (old_value and not new_value):
                    raise CorrectConsentValueMisMatchError(
                        'Both the old and new value must '
                        f'be provided. Got \'{old_value}\' and \'{new_value}\'.'
                        f' See {field.name}')
                elif old_value and new_value and old_value == new_value:
                    raise CorrectConsentValueMisMatchError(
                        'The old and new value can not be equal. '
                        f'Got \'{old_value}\' and \'{new_value}\'. '
                        f'See {field.name}')

    def registered_subject(self, subject_identifier=None):
        """Return registered subject.
        """
        try:
            registered_subject = RegisteredSubject.objects.get(
                subject_identifier=subject_identifier)
        except RegisteredSubject.DoesNotExist:
            raise ValidationError(
                'Missing registered subject for subject identifier '
                f'{subject_identifier}')
        else:
            return registered_subject

    def validate_old_values_agaist_registered_subject(
            self, old_value=None, db_value=None,
            attr_name=None, subject_identifier=None):
        """Validate old values entered against the registered subject.
        """
        if not getattr(self.registed_subject(subject_identifier=subject_identifier), attr_name) == old_value:
            raise CorrectConsentValueMisMatchError(
                f'Registered subject existing value: {db_value} does not match the '
                f'old value: {old_value} entered for field: {attr_name}.')
