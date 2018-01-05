from django_pandas.io import read_frame

from django.apps import apps as django_apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Export data to csv.'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='app_name.model')

    def handle(self, *args, **options):
        model = options['model']
        app_label, model_name = model.split('.')
        model_class = django_apps.get_model(app_label, model_name)
        self.stdout.write(
            self.style.NOTICE(f'Preparing to dump {model} objects to csv'))
        qs = model_class.objects.all()
        self.stdout.write(
            self.style.NOTICE(f'Total objects: {qs.count()}'))
        df = read_frame(qs)
        df.to_csv(f'{model_name}.csv', encoding='utf-8')
        self.stdout.write(
            self.style.SUCCESS(f'Done exporting {model_name} to csv.'))
