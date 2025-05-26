import calendar
from datetime import datetime
from selenium.common import NoSuchElementException, TimeoutException
from utils.Loging import logger
from config.driver_manager import driver, close_driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# from TripSelection import SelectablePlace_Oneway_RoundTrip
# from TripSelection import Selectable_MultiCity
# from TripSelection import Selectable_Date


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutccentureomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class BasicConfig:

    def close_login_panel(self):
        try:
            close_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="SW"]')))
            close_button.click()
            time.sleep(2)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            logger.error(f"Login Panel Exception: {e}")

    @staticmethod
    def is_valid_date_range(departure_date, return_date):
        """
        Checks if departure_date is earlier than return_date.
        :param departure_date: String in 'DD Mon YYYY' format (e.g., '20 Mar 2025')
        :param return_date: String in 'DD Mon YYYY' format (e.g., '25 Mar 2025')
        :return: True if valid, False otherwise
        """
        dep_date = datetime.strptime(departure_date, "%d %b %Y")  # Convert to datetime
        ret_date = datetime.strptime(return_date, "%d %b %Y")  # Convert to datetime
        return dep_date < ret_date  # Ensure departure is before return

    def Travellers_and_class(self, Adults, Children, Infants, travel_class):
        logger.info(
            f"\nAdults: 12+ years\nChildren: 2y-12y\nInfants: below 2y\n Travel Class:\n   if Economy Enter 0,\n   if Premium Economy Enter 1,\n   if Business Enter 2,\n   if First Class Enter 3")
        selecting_traveller_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'travellers')]")))
        selecting_traveller_button.click()

        if Adults == 1:
            one_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-1')]")))
            one_adult.click()
        elif Adults == 2:
            two_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-2')]")))
            two_adult.click()
        elif Adults == 3:
            three_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-3')]")))
            three_adult.click()
        elif Adults == 4:
            four_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-4')]")))
            four_adult.click()
        elif Adults == 5:
            five_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-5')]")))
            five_adult.click()
        elif Adults == 6:
            six_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-6')]")))
            six_adult.click()
        elif Adults == 7:
            seven_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-7')]")))
            seven_adult.click()
        elif Adults == 8:
            eight_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-8')]")))
            eight_adult.click()
        elif Adults == 9:
            nine_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'adults-9')]")))
            nine_adult.click()
        else:
            more_adult = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'gbTravelTooltip')]")))
            more_adult.click()

        # Children
        if Children == 0:
            no_child = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'children-0')]")))
            no_child.click()
        elif Children == 1:
            one_child = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'children-1')]")))
            one_child.click()
        elif Children == 2:
            two_child = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'children-2')]")))
            two_child.click()
        elif Children == 3:
            three_child = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'children-3')]")))
            three_child.click()
        elif Children == 4:
            four_child = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'children-4')]")))
            four_child.click()
        elif Children == 5:
            five_child = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'children-5')]")))
            five_child.click()
        elif Children == 6:
            six_child = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'children-6')]")))
            six_child.click()

        else:
            more_child = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//li[contains(@data-cy,'children-7')]")))
            more_child.click()

        # Infants
        if Infants == 0:
            no_infant = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'infants-0')]")))
            no_infant.click()
        elif Infants == 1:
            one_infant = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'infants-1')]")))
            one_infant.click()
        elif Infants == 2:
            two_infant = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'infants-2')]")))
            two_infant.click()
        elif Infants == 3:
            three_infant = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'infants-3')]")))
            three_infant.click()
        elif Infants == 4:
            four_infant = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'infants-4')]")))
            four_infant.click()
        elif Children == 5:
            five_infant = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'infants-5')]")))
            five_infant.click()
        elif Children == 6:
            six_infant = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'infants-6')]")))
            six_infant.click()

        else:
            more_infant = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'infants-7')]")))
            more_infant.click()

        # Travel Class
        if travel_class == 0:
            economy = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'travelClass-0')]")))
            economy.click()
        elif travel_class == 1:
            premium_economy = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'travelClass-1')]")))
            premium_economy.click()
        elif travel_class == 2:
            business = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'travelClass-2')]")))
            business.click()
        else:
            first_class = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@data-cy,'travelClass-3')]")))
            first_class.click()

        apply_changes = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@data-cy,'travellerApplyBtn')]")))
        apply_changes.click()

    def special_fare(self, Select_fare):
        logger.info(
            "Special Fare Offer:   \nif Regular enter 0\n   if Student Enter 1\n   if Senior Citizen Enter 2\n   if Armed Forec Enter 3\n   if Doctor and Nurse Enter 4")
        if Select_fare == 0:
            regular = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Regular')]")))
            regular.click()
        elif Select_fare == 1:
            student = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Student')]")))
            student.click()
        elif Select_fare == 2:
            senior = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Senior')]")))
            senior.click()
        elif Select_fare == 3:
            armed_force = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Armed')]")))
            armed_force.click()
        else:
            doctor_nurse = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Doctor')]")))
            doctor_nurse.click()

    def TravelClass_and_specialOffer(self):
        basic_config = BasicConfig()
        basic_config.special_fare(1)
        basic_config.Travellers_and_class(2, 8, 0, 1)


class Select_trip:

    def select_trip_type(self, trip_type):


        try:
            if trip_type == 'multicity':
                logger.info(f"Successfully Selected: {trip_type}")
                select_multicity = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'Multi City')]")))
                select_multicity.click()

                basic_config = BasicConfig()
                basic_config.TravelClass_and_specialOffer()
                time.sleep(2)
                selecting_places = Selectable_MultiCity()
                selecting_places.departure_from_place('Bengaluru')
                selecting_places.to_departure_place('Delhi', 'sion')
                selecting_date = Selectable_Date()
                selecting_date.departure_date('03', 'Sept', '2025')
                time.sleep(20)


            elif trip_type == 'oneway':
                logger.info(f"Successfully Selected: {trip_type}")
                select_oneway = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'One Way')]")))
                select_oneway.click()

                basic_config = BasicConfig()
                basic_config.TravelClass_and_specialOffer()
                time.sleep(2)
                selecting_places = SelectablePlace_Oneway_RoundTrip()
                selecting_places.from_departure_place('Bengaluru')
                selecting_places.to_departure_place('Delhi')
                selecting_date = Selectable_Date()
                selecting_date.departure_date('30', 'July', '2025')
                time.sleep(20)


            else:
                logger.info(f"Successfully Selected: {trip_type}")
                select_roundtrip = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'Round Trip')]")))
                select_roundtrip.click()

                basic_config = BasicConfig()
                basic_config.TravelClass_and_specialOffer()
                time.sleep(2)
                selecting_places = SelectablePlace_Oneway_RoundTrip()
                selecting_places.from_departure_place('Bengaluru')
                selecting_places.to_departure_place('Delhi')
                selecting_date = Selectable_Date()
                selecting_date.departure_date('05', 'July', '2025')
                selecting_date.return_date('05', 'August', '2025', '05 July 2025')
                time.sleep(20)

        except Exception as e:
            logger.error(f"Trip Type Select Function Error: {e}")


class Selectable_places:

    def from_departure_place_multicity(self, from_departure):
        # From which Place
        from_place1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@data-cy,'fromAnotherCity0')]")))
        from_place1.click()
        time.sleep(2)

        focus_from_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'react-autosuggest__input')]")))
        focus_from_place.send_keys(from_departure)
        time.sleep(2)

        place_dropdown_list = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
        place_dropdown_list.click()
        logger.info("successfully selected --- From --- place")


# ************************************************************************************************************************************************************************************

class SelectablePlace_Oneway_RoundTrip:

    def from_departure_place(self, from_departure):
        # From Place
        from_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'fromCity')]")))
        from_place.click()
        time.sleep(2)

        focus_from_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'react-autosuggest__input')]")))
        focus_from_place.send_keys(from_departure)
        time.sleep(2)

        place_dropdown_list = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
        place_dropdown_list.click()
        logger.info("Successfully selected --- From --- place")

    def to_departure_place(self, to_departure):
        # To Place
        to_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'toCity')]")))
        to_place.click()
        focus_to_place = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
        focus_to_place.send_keys(to_departure)
        place_dropdown_list = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
        place_dropdown_list.click()
        time.sleep(5)
        logger.info("Successfully selected  --- To  --- place")


class Selectable_MultiCity:
    def departure_from_place(self, fromCity1):
        logger.info("Please Select From Cities: \nIf willing to add one more city, Please Enter 1")

        # From Place City1
        from_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'fromAnotherCity0')]")))
        from_place.click()
        time.sleep(2)

        focus_from_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
        focus_from_place.send_keys(fromCity1)
        time.sleep(2)

        place_dropdown_list = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
        place_dropdown_list.click()
        logger.info("Successfully selected --- From --- First place")

    def AddCity(self, add_another_city, ToCity):
        if add_another_city == 1:
            add_city = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@data-cy,'addAnotherCity')]")))
            add_city.click()

            # From Place City1
            to_place = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'toAnotherCity2')]")))
            to_place.click()
            time.sleep(2)

            focus_to_place = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
            focus_to_place.send_keys(ToCity)
            time.sleep(2)

            place_dropdown_list = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
            place_dropdown_list.click()
            logger.info("Successfully selected --- From --- First place")


        else:
            logger.info("No Add-on city option was selected")

    def to_departure_place(self, ToCity1, ToCity2):
        # To Place City1
        to_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'toAnotherCity0')]")))
        to_place.click()
        time.sleep(2)

        focus_to_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
        focus_to_place.send_keys(ToCity1)
        time.sleep(2)

        place_dropdown_list = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
        place_dropdown_list.click()
        logger.info("Successfully selected --- From --- First place")

        # To Place City2
        to_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'toAnotherCity1')]")))
        to_place.click()
        time.sleep(2)

        focus_to_place = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
        focus_to_place.send_keys(ToCity2)
        time.sleep(2)

        place_dropdown_list = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
        place_dropdown_list.click()
        logger.info("Successfully selected --- From --- First place")


class Selectable_Date:

    def departure_date(self, depart_Date, depart_Month, depart_Year):
        # Click on date selector/picker button
        departure_selector = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@class, 'flt_fsw_inputBox dates inactiveWidget ')]")))
        departure_selector.click()

        # pick month and year
        while True:
            short_month = calendar.month_abbr[list(calendar.month_name).index(depart_Month)]
            global departure_target_date
            departure_target_date = f"{short_month} {depart_Date} {depart_Year}"
            date_pick_container = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'DayPicker-Months')]"))).text
            if depart_Month in date_pick_container and depart_Year in date_pick_container:
                pick_date = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"//div[contains(@aria-label, '{departure_target_date}')]")))
                pick_date.click()
                break

            else:
                next_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(@class, 'DayPicker-NavButton DayPicker-NavButton--next')]")))
                next_button.click()
        logger.info(f"Successfully selected Departure date")

    def return_date(self, return_Date, return_Month, return_Year, departure_date=departure_target_date):
        return_target_date = f"{return_Date} {return_Month} {return_Year}"
        # departure_date = dep
        if not BasicConfig.is_valid_date_range(departure_date, return_target_date):
            logger.info("Invalid date range: Return date must be after departure date.")
            return
        # Click on date selector/picker button
        departure_selector = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@class, 'flt_fsw_inputBox dates reDates inactiveWidget ')]")))
        departure_selector.click()

        # check return matches with departure date

        # pick month and year
        while True:
            try:
                short_month = calendar.month_abbr[list(calendar.month_name).index(return_Month)]
                print(short_month)
            except ValueError:
                logger.error(f"Invalid month abbreviation: {return_Month}")
                return
            return_target_date = f"{short_month} {return_Date} {return_Year}"
            date_pick_container = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(@class, 'DayPicker Selectable Range')]"))).text
            if return_Month and return_Year in date_pick_container:
                pick_date = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"//div[contains(@aria-label, '{return_target_date}')]")))
                pick_date.click()

            else:
                next_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(@class, 'DayPicker-NavButton DayPicker-NavButton--next')]")))
                next_button.click()
                time.sleep(3)
            logger.info(f"Successfully selected Return date")


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/flights/")
    logger.info("Opening the link")
    driver.maximize_window()
    time.sleep(5)

    basic_config = BasicConfig()
    basic_config.close_login_panel()
    select_trip = Select_trip()
    select_trip.select_trip_type('roundtrip')
