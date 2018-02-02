from datetime import date, timedelta

from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES
from edc_registration.models import RegisteredSubject

from ..models import (
    CorrectConsent, DeceasedMember, MovedMember, SubjectDoesNotExistError)


class TestValidateSubjectIdentifier(TestCase):

    def setUp(self):

        self.options = dict(
            subject_identifier='006-11111111-11',
            report_datetime=get_utcnow())
        registered_subject_options = dict(
            dob=date(1992, 7, 6),
            first_name='TEST',
            gender='M',
            identity='702216628',
            identity_or_pk='702216628',
            identity_type='OMANG',
            initials='RP',
            is_dob_estimated='-',
            last_name='TEST',
            registration_identifier='3f4ce583bf1944ea8565203321091d56',
            study_site='35',
            subject_identifier='006-11111111-11')
        self.registered_subject = RegisteredSubject.objects.create(
            **registered_subject_options)

    def test_invalid_subject_identifier_consent(self):
        """Assert that an errors is thrown if no valid subject identifier is
        used to create a correct consent.
        """
        subject_identifier = '006-11111111-22'
        expected_message = 'Subject with subject identifier: '\
            f'{subject_identifier} does not exist.'
        self.options.update(
            subject_identifier=subject_identifier,
            old_last_name='TEST',
            new_last_name='TESTING')
        with self.assertRaisesMessage(SubjectDoesNotExistError, expected_message):
            CorrectConsent.objects.create(**self.options)

    def test_valid_subject_identifier_consent(self):
        """Assert that no error is thrown if a valid subject identifier is
        used to create a correct consent.
        """
        self.options.update(
            old_last_name='TEST',
            new_last_name='TESTING')
        CorrectConsent.objects.create(**self.options)

    def test_valid_subject_identifier_moved(self):
        """Assert that no error is thrown if a valid subject identifier is
        used to create a correct consent.
        """
        self.options.update(
            time_point='T1',
            moved_household=YES,
            moved_community=YES,
            new_community='sebina',
            update_locator=NO)
        MovedMember.objects.create(**self.options)

    def test_valid_subject_identifier_deceased(self):
        """Assert that no error is thrown if a valid subject identifier is
        used to create a correct consent.
        """
        self.options.update(
            time_point='T1',
            death_date=date.today() + timedelta(days=10),
            site_aware_date=get_utcnow(),
            death_cause='Car accident',
            duration_of_illness=0,
            relationship_death_study='Definitely not related')
        DeceasedMember.objects.create(**self.options)

    def test_invalid_subject_identifier_moved(self):
        """Assert that an errors is thrown if no valid subject identifier is
        used to create a moved member.
        """
        subject_identifier = '006-11111111-22'
        expected_message = 'Subject with subject identifier: '\
            f'{subject_identifier} does not exist.'
        self.options.update(
            subject_identifier=subject_identifier,
            time_point='T1',
            moved_household=YES,
            moved_community=YES,
            new_community='sebina',
            update_locator=NO)
        with self.assertRaisesMessage(SubjectDoesNotExistError, expected_message):
            MovedMember.objects.create(**self.options)

    def test_invalid_subject_identifier_deceased(self):
        """Assert that an errors is thrown if no valid subject identifier is
        used to create a deceased member.
        """
        subject_identifier = '006-11111111-22'
        expected_message = 'Subject with subject identifier: '\
            f'{subject_identifier} does not exist.'
        self.options.update(
            subject_identifier=subject_identifier,
            time_point='T1',
            death_date=date.today() + timedelta(days=10),
            site_aware_date=get_utcnow(),
            death_cause='Car accident',
            duration_of_illness=0,
            relationship_death_study='Definitely not related')
        with self.assertRaisesMessage(SubjectDoesNotExistError, expected_message):
            DeceasedMember.objects.create(**self.options)
