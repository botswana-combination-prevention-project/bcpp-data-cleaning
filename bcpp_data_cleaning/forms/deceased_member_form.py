from django import forms

from ..models import DeceasedMember


class DeceasedMemberForm (forms.ModelForm):

    class Meta:
        model = DeceasedMember
        fields = '__all__'
