from django.contrib import admin

from ..admin_site import bcpp_data_cleaning_admin
from ..forms import CorrectConsentForm
from ..models import CorrectConsent


@admin.register(CorrectConsent, site=bcpp_data_cleaning_admin)
class CorrectConsentAdmin(admin.ModelAdmin):

    form = CorrectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'consent_version',
                'report_datetime',
                'old_identity',
                'new_identity',
                'old_last_name',
                'new_last_name',
                'old_first_name',
                'new_first_name',
                'old_initials',
                'new_initials',
                'old_dob',
                'new_dob',
                'old_gender',
                'new_gender',
                'old_guardian_name',
                'new_guardian_name',
                'old_may_store_samples',
                'new_may_store_samples',
                'old_is_literate',
                'new_is_literate',
                'new_witness_name',
                'old_witness_name',
            )}),
    )

    list_display = ('subject_identifier', 'report_datetime')

    list_filter = ('report_datetime', 'created', 'modified', 'consent_version')

    search_fields = (
        'subject_identifier',
        'new_first_name',
        'old_first_name',
        'new_last_name',
        'old_last_name')

    radio_fields = {
        'consent_version': admin.VERTICAL,
        'old_gender': admin.VERTICAL,
        'new_gender': admin.VERTICAL,
        'old_is_literate': admin.VERTICAL,
        'new_is_literate': admin.VERTICAL,
        'old_may_store_samples': admin.VERTICAL,
        'new_may_store_samples': admin.VERTICAL,
    }
