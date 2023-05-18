from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class FlightsPage(BaseClass):

    DISCOUNT_CODE = (By.CSS_SELECTOR, "#bkmgFlights_promoCodeToggle")
    RADIO_BUTTONS = (By.XPATH, "//input[@type='radio']")
    DEPARTURE = (By.XPATH, "//input[@id='bkmgFlights_origin_trip_1']")
    ARRIVAL = (By.XPATH, "//input[@id='bkmgFlights_destination_trip_1']")
    CITIES = (By.XPATH, "//li[@role='option']//div//div//span[@class='location-city-name ng-star-inserted']")
    ARRIVAL_AIRPORT = (By.XPATH, "//li[@role='option']//div//div//span[@class='location-airport-name']")
    TRAVEL_DATE_FIELD_DEPARTURE = (By.XPATH, "//input[@aria-label='Departure']")
    PASSENGERS_DROPDOWN = (By.XPATH, "//button[@id='bkmgFlights_selectTravelers']")
    ADD_ADULT = (By.XPATH, "//button[@aria-label='Add one adult']")
    CLOSE_PASSENGER_SELECTION = (By.XPATH, "//button[@id='bkmgFlights_selectTravelers_confirmTravelers']")
    NUMBER_OF_PASSENGERS = (By.XPATH, "//span[@class='text-capitalize']")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='bkmgFlights_findButton']")


    def __init__(self, driver):
        self.driver = driver

    # def get_departure(self):
    #     return self.driver.find_element(*FlightsPage.DEPARTURE_DATE)

    def get_discount(self):
        return self.driver.find_element(*FlightsPage.DISCOUNT_CODE)

    def get_flight_type(self):
        radio_buttons = self.driver.find_elements(*FlightsPage.RADIO_BUTTONS)
        flight_type = []
        for type_of in radio_buttons:
            type_of.click()
            flight_type.append(type_of.get_attribute('value'))
        return flight_type

    def select_flight_type(self):
        radio = self.driver.find_elements(*FlightsPage.RADIO_BUTTONS)
        for item in radio:
            if item.get_attribute('value') == 'R':
                item.click()

    def select_departure(self):
        from_field = self.driver.find_element(*FlightsPage.DEPARTURE)
        self.scroll_page(500)
        from_field.send_keys('Cal')
        self.verify_presence(By.XPATH, "//li[@role='option']//div//div//span[@class='location-city-name ng-star-inserted']")
        cities_list = self.driver.find_elements(*FlightsPage.CITIES)
        index = 1
        for city in cities_list:
            if city.text == "Calgary":
                self.driver.find_element(By.XPATH,f"//li[@role='option'][{index}]").click()
                return city.text
            else:
                index += 1
        return -1

    def select_arrival(self):
        to_field = self.driver.find_element(*FlightsPage.ARRIVAL)
        to_field.send_keys('Van')
        self.verify_presence(By.XPATH, "//li[@role='option']//div//div//span[@class='location-city-name ng-star-inserted']")
        city_list = self.driver.find_elements(*FlightsPage.CITIES)
        city_index = 1
        airport_index = 1
        index = 0
        for city in city_list:
            if city.text == "Vancouver":
                airports = self.driver.find_elements(*FlightsPage.ARRIVAL_AIRPORT)
                for airport in airports:
                    if airport.text == "Vancouver Int.":
                        index = city_index + airport_index
                        self.driver.find_element(By.XPATH,f"//li[@role='option'][{index}]").click()
                        return airport.text
                else:
                    airport_index += 1
            else:
                city_index += 1
        return -1

    def select_travel_dates(self, date_leave, date_return):
        months_dict = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }

        self.driver.find_element(*FlightsPage.TRAVEL_DATE_FIELD_DEPARTURE).click()
        departure_year = date_leave[0:4]
        month_leave = months_dict[date_leave[5:7]]
        while True:
            try:
                self.driver.find_element(By.XPATH,f"//caption[normalize-space()='{month_leave + ' ' + departure_year }']")
                break
            except:
                self.driver.find_element(By.XPATH,"//button[@id='bkmgFlights_travelDates_1_nextMonth']").click()

        self.driver.find_element(By.XPATH,f"//div[@id='bkmgFlights_travelDates_1-date-{date_leave[0:10]}']").click()

        return_year = date_return[0:4]
        month_return = months_dict[date_return[5:7]]
        while True:
            try:
                self.driver.find_element(By.XPATH,f"//caption[normalize-space()='{month_return + ' ' + return_year }']")
                break
            except:
                self.driver.find_element(By.XPATH,"//button[@id='bkmgFlights_travelDates_1_nextMonth']").click()

        self.driver.find_element(By.XPATH,f"//div[@id='bkmgFlights_travelDates_1-date-{date_return[0:10]}']").click()

        self.driver.find_element(By.XPATH,"//button[@id='bkmgFlights_travelDates_1_confirmDates']").click()

    def select_passengers(self):
        passenger_button = self.driver.find_element(*FlightsPage.PASSENGERS_DROPDOWN)
        passenger_button.click()
        self.driver.find_element(*FlightsPage.ADD_ADULT).click()
        self.driver.find_element(*FlightsPage.CLOSE_PASSENGER_SELECTION).click()
        return self.driver.find_element(*FlightsPage.NUMBER_OF_PASSENGERS).text

    def search_flights(self):
        self.driver.find_element(*FlightsPage.SEARCH_BUTTON).click()
        self.verify_presence(By.CSS_SELECTOR, "#flightBlockMainTitle")
        return self.driver.title











