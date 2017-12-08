from django.contrib import admin

from ..admin_site import bcpp_data_cleaning_admin
from ..forms import DeceasedMemberForm
from ..models import DeceasedMember
from .model_admin_mixin import ModelAdminMixin


@admin.register(DeceasedMember, site=bcpp_data_cleaning_admin)
class DeceasedMemberAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DeceasedMemberForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'time_point',
                'report_datetime',
                'death_date',
                'site_aware_date',
                'death_cause',
                'duration_of_illness',
                'relationship_death_study')}),
    )

    list_display = ('subject_identifier', 'time_point', 'report_datetime')

    search_fields = [
        'subject_identifier']

    list_filter = (
        'report_datetime', 'time_point')

    radio_fields = {
        "time_point": admin.VERTICAL,
        'relationship_death_study': admin.VERTICAL
    }
