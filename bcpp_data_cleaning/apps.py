from datetime import datetime
from dateutil.tz import gettz

from django.apps import AppConfig as DjangoAppConfig

from edc_base.address import Address
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_base.utils import get_utcnow
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig


class AppConfig(DjangoAppConfig):
    name = 'bcpp_data_cleaning'
    base_template_name = 'edc_base/base.html'
    project_title = 'BCPP Data Cleaning'
    project_name = 'BCPP Data Cleaning'
    institution = 'Botswana Harvard Partneship'

    name = 'bcpp_data_cleaning'
    admin_site_name = 'bcpp_data_cleaning_admin'
    include_in_administration_section = True


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'BCPP DATA CLEANING'
    institution = 'Botswana-Harvard AIDS Institute Partnership'
    copyright = f'2013-{get_utcnow().year}'
    license = 'GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007'
    physical_address = Address(
        company_name='Botswana-Harvard AIDS Institute Partnership',
        address='Plot 1836',
        city='Gaborone',
        country='Botswana',
        tel='+267 3902671',
        fax='+267 3901284')
    postal_address = Address(
        company_name='Botswana-Harvard AIDS Institute Partnership',
        address='Private Bag BO 320',
        city='Bontleng',
        country='Botswana')


class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = '066'


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP066'
    protocol_number = '066'
    protocol_name = 'BCPP'
    protocol_title = 'Botswana Combination Prevention Project'

    study_open_datetime = datetime(2013, 10, 18, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(2018, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))
