from datetime import datetime
from dateutil.tz import gettz

from django.apps import AppConfig as DjangoAppConfig

from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap


class AppConfig(DjangoAppConfig):
    name = 'bcpp_data_cleaning'
    base_template_name = 'edc_base/base.html'
    project_title = 'BCPP Data Cleaning'
    project_name = 'BCPP Data Cleaning'
    institution = 'Botswana Harvard Partneship'


class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = '066'


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP066'
    protocol_number = '066'
    protocol_name = 'BCPP'
    protocol_title = 'Botswana Combination Prevention Project'

    study_open_datetime = datetime(2013, 10, 18, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(2018, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))
