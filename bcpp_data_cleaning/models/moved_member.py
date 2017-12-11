from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO_UNKNOWN

from .validate_subject_identifier_model_mixin import ValidateSybjectidentifierModelMixin

TIME_POINT = (
    ('T0', 'T0'),
    ('T1', 'T1'),
    ('T2', 'T2')
)


class MovedMember(ValidateSybjectidentifierModelMixin, BaseUuidModel):

    """A model completed by the user to indicate a subject has
    moved from the household and or community.
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

    moved_household = models.CharField(
        max_length=7,
        verbose_name='Has the participant moved out of the household where last seen',
        choices=YES_NO_UNKNOWN,
        null=True,
        blank=False,
        help_text=""
    )

    moved_community = models.CharField(
        max_length=7,
        verbose_name='Has the participant moved out of the community',
        choices=YES_NO_UNKNOWN,
        null=True,
        blank=False,
        help_text=""
    )

    new_community = models.CharField(
        max_length=50,
        verbose_name='If the participant has moved, provide the name of the new community',
        null=True,
        blank=True,
        help_text="If moved out of the community, provide a new community name or \'UNKNOWN\'"
    )

    update_locator = models.CharField(
        max_length=7,
        verbose_name='Has the locator information changed',
        choices=YES_NO_UNKNOWN,
        null=True,
        blank=False,
        help_text=('If YES, please enter the changed information '
                   'the locator form')
    )

    comment = models.TextField(
        verbose_name="Comment",
        max_length=250,
        blank=True,
        help_text=('')
    )

    def __str__(self):
        return f'{self.subject_identifier}, {self.time_point}'

    def save(self, *args, **kwargs):
        self.vaidate_subject_identifier(
            subject_identifier=self.subject_identifier)
        super(MovedMember, self).save(*args, **kwargs)

    class Meta:
        app_label = 'bcpp_data_cleaning'
        unique_together = ('subject_identifier', 'time_point')
