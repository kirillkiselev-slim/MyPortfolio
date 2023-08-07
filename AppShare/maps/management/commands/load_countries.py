import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from maps.models import Location
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Load data from CSV file'
    def handle(self, *args, **kwargs):
        csv_file =  settings.BASE_DIR / 'data' / 'CountriesCoordinates.csv'

        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                country = row['country']
                latitude = float(row['latitude'])
                longitude = float(row['longitude'])


                Location.objects.get_or_create(
                    country=country,
                    latitude=latitude,
                    longitude=longitude,
                )
