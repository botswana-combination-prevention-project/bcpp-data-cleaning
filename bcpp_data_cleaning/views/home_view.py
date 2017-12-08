from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from ..models import CorrectConsent, DeceasedMember, MovedMember


class HomeView(EdcBaseViewMixin, TemplateView):

    app_config_name = 'bcpp_data_cleaning'
    template_name = 'bcpp_data_cleaning/home.html'
    app_config = django_apps.get_app_config('bcpp_data_cleaning')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        moved_members = MovedMember.objects.all().count()
        correct_consents = CorrectConsent.objects.all().count()
        deceased_members = DeceasedMember.objects.all().count()
        context.update(
            project_name=self.app_config.project_name,
            project_title=self.app_config.project_title,
            institution=self.app_config.institution,
            deceased_members=deceased_members,
            correct_consents=correct_consents,
            moved_members=moved_members)
        return context
