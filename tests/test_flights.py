from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pageObjects.FlightsPage import FlightsPage
import datetime


class TestFlights(BaseClass):

    def test_verify_flight_types(self):
        log = self.get_logger()
        flights_page = FlightsPage(self.driver)
        self.verify_presence(By.CSS_SELECTOR, "#bkmgFlights_promoCodeToggle")
        types_found = flights_page.get_flight_type()
        verification_list = ['M', 'R', 'O']
        log.info(f"Types of flights found {types_found}")
        assert all(item in types_found for item in verification_list), log.error(f"Types of flights found {types_found}")

    def test_add_departure(self):
        flights_page = FlightsPage(self.driver)
        # self.scroll_page(2000)
        flights_page.select_flight_type()
        departure_city = flights_page.select_departure()
        assert departure_city == "Calgary"

    def test_add_arrival(self):
        flights_page = FlightsPage(self.driver)
        arrival_airport = flights_page.select_arrival()
        assert arrival_airport == "Vancouver Int."

    def test_select_travel_dates(self):
        flights_page = FlightsPage(self.driver)
        today_date = datetime.datetime.today()
        departure_date = today_date + datetime.timedelta(days=14)
        return_date = departure_date + datetime.timedelta(days=7)
        flights_page.select_travel_dates(str(departure_date), str(return_date))

    def test_select_passengers(self):
        flights_page = FlightsPage(self.driver)
        number_of_passengers = flights_page.select_passengers()
        assert number_of_passengers == "2 Adults"

    def test_search_flights(self):
        flights_page = FlightsPage(self.driver)
        next_page_title = flights_page.search_flights()
        print(next_page_title)
        assert next_page_title == 'Air Canada - Select Flights'





