from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'bcpp_data_cleaning'
    base_template_name = 'edc_base/base.html'
    project_title = 'BCPP Data Cleaning'
    project_name = 'BCPP Data Cleaning'
    institution = 'Botswana Harvard Partneship'
