# Zus Django Project

This is a Django project named "zus" with a scraper app.

## Getting Started

1. Clone the [repository](https://github.com/SohaibAnwaar/zue_coffee_scraping_backend).
2. CD into the project folder: `cd zus`.
3. Create a virtual environment: `python -m venv venv` and activate it.
4. Install dependencies: `pip install -r requirements.txt`.
5. Apply migrations: `python manage.py migrate`.
6. Get a Google Maps API key:
   - Visit [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the "Maps JavaScript API" for your project.
   - Create an API key and restrict its usage if necessary.
7. Create an `.env` file:
   - Copy the contents of `.env_example` into a new file named `.env`.
   - Add your Google Maps API key to the `.env` file.
8. Run the management command to scrape data:
   ```bash
   python manage.py scrape_zuscoffee
9. Run the development server: `python manage.py runserver`
10. Go to the URL http://localhost:8000/api/coffee-shops/ to view the scraped coffee shop data.
