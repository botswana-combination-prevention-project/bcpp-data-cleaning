from django.test import TestCase

from edc_base.utils import get_utcnow

from ..models import CorrectConsent, CorrectConsentValueMisMatchError


class TestCorrectConsent(TestCase):

    def setUp(self):

        self.options = dict(
            subject_identifier='11111111',
            report_datetime=get_utcnow())

    def test_only_new_value_provided(self):
        """Assert if new value provided without an old value throws an error.
        """
        new_last_name = 'TESTING'
        expected_message = 'Both the old and new value must be provided. '\
            f'Got \'None\' and \'{new_last_name}\'. See old_last_name'
        self.options.update(new_last_name=new_last_name)
        with self.assertRaisesMessage(CorrectConsentValueMisMatchError, expected_message):
            CorrectConsent.objects.create(**self.options)

    def test_only_old_value_provided(self):
        """Assert if old value provided without an new value throws an error.
        """
        old_last_name = 'TEST'
        expected_message = 'Both the old and new value must be provided. '\
            f'Got \'{old_last_name}\' and \'None\'. See old_last_name'
        self.options.update(old_last_name=old_last_name)
        with self.assertRaisesMessage(CorrectConsentValueMisMatchError, expected_message):
            CorrectConsent.objects.create(**self.options)

    def test_old_and_new_value_same(self):
        """Assert if both old and new value are the same an error is thrown.
        """
        new_last_name = 'TEST'
        old_last_name = 'TEST'
        expected_message = 'The old and new value can not be equal. '\
            f'Got \'{new_last_name}\' and \'{old_last_name}\'. See old_last_name'
        self.options.update(
            old_last_name=old_last_name, new_last_name=new_last_name)
        with self.assertRaisesMessage(CorrectConsentValueMisMatchError, expected_message):
            CorrectConsent.objects.create(**self.options)
