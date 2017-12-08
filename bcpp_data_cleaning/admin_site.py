from django.contrib.admin import AdminSite


class BcppDataCleaningAdminSite(AdminSite):
    site_title = 'BCPP Data Cleaning'
    site_header = 'BCPP Data Cleaning'
    index_title = 'BCPP Data Cleaning'
    site_url = '/bcpp_data_cleaning/list/'


bcpp_data_cleaning_admin = BcppDataCleaningAdminSite(
    name='bcpp_data_cleaning_admin')
