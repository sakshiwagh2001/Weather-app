from django.core.management.base import BaseCommand
import requests
from weather_data.models import WeatherRecord

REGIONS = ['UK', 'England', 'Scotland', 'Wales']
PARAMETERS = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall']

class Command(BaseCommand):
    help = 'Fetch and save weather data from Met Office'

    def handle(self, *args, **kwargs):
        base_url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{param}/date/{region}.txt'

        for parameter in PARAMETERS:
            for region in REGIONS:
                url = base_url.format(param=parameter, region=region)
                print(f"\nFetching {parameter} data for {region} from {url}")

                try:
                    response = requests.get(url)
                    response.raise_for_status()
                except requests.RequestException as e:
                    print(f"Failed to fetch data for {region}-{parameter}: {e}")
                    continue

                lines = response.text.splitlines()[5:]  # skip headers

                for line in lines:
                    if not line.strip():
                        continue
                    parts = line.split()
                    if len(parts) < 13 or not parts[0].isdigit():
                        continue
                    
                    try:
                        record = WeatherRecord(
                            region=region,
                            parameter=parameter,
                            year=int(parts[0]),
                            jan=float(parts[1]),
                            feb=float(parts[2]),
                            mar=float(parts[3]),
                            apr=float(parts[4]),
                            may=float(parts[5]),
                            jun=float(parts[6]),
                            jul=float(parts[7]),
                            aug=float(parts[8]),
                            sep=float(parts[9]),
                            oct=float(parts[10]),
                            nov=float(parts[11]),
                            dec=float(parts[12]),
                            annual=float(parts[13]) if len(parts) > 13 and parts[13] != '---' else None
                        )
                        print(f"Saving: {record}")
                        record.save()
                    except Exception as e:
                        print(f"Error parsing line: {e}")


