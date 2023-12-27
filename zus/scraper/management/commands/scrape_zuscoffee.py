import time

import googlemaps
import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from ...models import CoffeeShop
from django.conf import settings


class Command(BaseCommand):
    help = 'Scrape zuscoffee.com and load data into the database'

    def handle(self, *args, **options):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
        }
        base_url = "https://zuscoffee.com/category/store/melaka/page/"
        page = 1
        objects = []

        while True:
            url = f"{base_url}{page}/"
            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            except requests.exceptions.HTTPError as err:
                self.stdout.write(self.style.ERROR(f"HTTP Error: {err}"))
                break
            except requests.exceptions.RequestException as err:
                self.stdout.write(self.style.ERROR(f"Request Error: {err}"))
                break

            if response.status_code == 404:
                break
            else:
                self.stdout.write(f"Page {page} - Status Code: {response.status_code}")
                soup = BeautifulSoup(response.content, "html.parser")
                widget_container = soup.find("div", class_="ecs-posts elementor-posts-container elementor-posts elementor-grid elementor-posts--skin-archive_custom")
                cards = widget_container.find_all('article')

                for card in cards:
                    shop_data = self.extract_data(card)

                    name = shop_data.get('name')
                    location = shop_data.get('location')
                    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
                    breakpoint()
                    # Geocoding an address
                    try:
                        geocode_result = gmaps.geocode(location)
                    except Exception as e: # noqa
                        continue

                    if geocode_result:
                        coordinates = geocode_result[0]["geometry"]["location"]
                        latitude = coordinates["lat"]
                        longitude = coordinates["lng"]
                        try:
                            shop = CoffeeShop.objects.create(name=name, address=location, latitude=latitude, longitude=longitude)
                            objects.append(shop.id)
                        except Exception as e: # noqa
                            continue
                    else:
                        continue

            # Add a delay between requests to avoid overloading the server
            time.sleep(1)

            # Increment the page number for the next iteration
            page += 1

        if objects:
            self.stdout.write(self.style.SUCCESS(f"{len(objects)} loaded successfully!"))
        else:
            self.stdout.write(self.style.ERROR("Error"))

    def extract_data(self, card):
        rows = card.find_all("div", class_="elementor-row")
        name = rows[0].find("p").text
        location = rows[1].find("p").text
        return {"name": name, "location": location}
