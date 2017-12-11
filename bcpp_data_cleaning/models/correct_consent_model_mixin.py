
class CorrectConsentValueMisMatchError(Exception):
    pass


class CorrectConsentMixin:

    """A model linked to the subject consent to record corrections."""

    def compare_old_value_to_new_value(self):
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
