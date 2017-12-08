from django.contrib import admin

from ..admin_site import bcpp_data_cleaning_admin
from ..forms import MovedMemberForm
from ..models import MovedMember
from .model_admin_mixin import ModelAdminMixin


@admin.register(MovedMember, site=bcpp_data_cleaning_admin)
class MovedMemberAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MovedMemberForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'time_point',
                'report_datetime',
                'moved_household',
                'moved_community',
                'new_community',
                'update_locator',
                'comment')}),
    )

    list_display = (
        'subject_identifier',
        'time_point',
        'moved_household',
        'moved_community',
        'new_community',
        'update_locator',
    )

    search_fields = ['subject_identifier']

    list_filter = (
        'report_datetime', 'time_point',)

    radio_fields = {
        "time_point": admin.VERTICAL,
        "moved_household": admin.VERTICAL,
        "moved_community": admin.VERTICAL,
        "update_locator": admin.VERTICAL,
    }
