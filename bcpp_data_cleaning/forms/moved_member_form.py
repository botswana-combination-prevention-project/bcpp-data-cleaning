from django import forms

from edc_base.modelform_mixins import CommonCleanModelFormMixin
from edc_base.modelform_validators import FormValidatorMixin

from ..models import MovedMember


class MovedMemberForm(FormValidatorMixin, CommonCleanModelFormMixin, forms.ModelForm):
    pass

    class Meta:
        model = MovedMember
        fields = '__all__'
