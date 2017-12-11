from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import DEATH_RELATIONSIP_TO_STUDY

from .validate_subject_identifier_model_mixin import ValidateSybjectidentifierModelMixin


TIME_POINT = (
    ('T0', 'T0'),
    ('T1', 'T1'),
    ('T2', 'T2')
)


class DeceasedMember(ValidateSybjectidentifierModelMixin, BaseUuidModel):

    """A model completed by the user to report the death of a member.
    """

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    report_datetime = models.DateTimeField(
        verbose_name="Correction report date ad time",
        null=True,
        validators=[
            datetime_not_future],
    )

    time_point = models.CharField(
        max_length=3,
        verbose_name='Time point',
        choices=TIME_POINT,
        null=True,
        blank=False,
        help_text=""
    )

    death_date = models.DateField(
        verbose_name='Date of Death:',
        validators=[
            date_not_future],
        help_text='')

    site_aware_date = models.DateField(
        verbose_name='Date site aware of Death:',
        validators=[
            date_not_future],
        help_text='')

    death_cause = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name=(
            'Describe the major cause of death(including pertinent autopsy '
            'information if available),starting with the first noticeable '
            'illness thought to be related to death,continuing to '
            'time of death. '),
        help_text=(
            'Note: Cardiac and pulmonary arrest are not major reasons and '
            'should not be used to describe major cause'))

    duration_of_illness = models.IntegerField(
        verbose_name=(
            'Duration of acute illness directly causing death '
            '(in days, or choose Unknown)?'),
        help_text='in days',
        default=0)

    relationship_death_study = models.CharField(
        verbose_name='What is the relationship of the death to study participation?',
        max_length=50,
        choices=DEATH_RELATIONSIP_TO_STUDY,
        help_text='')

    def __str__(self):
        return f'{self.subject_identifier}, {self.time_point}'

    def save(self, *args, **kwargs):
        self.vaidate_subject_identifier(
            subject_identifier=self.subject_identifier)
        super(DeceasedMember, self).save(*args, **kwargs)

    class Meta:
        app_label = 'bcpp_data_cleaning'
        unique_together = ('subject_identifier', 'time_point')
