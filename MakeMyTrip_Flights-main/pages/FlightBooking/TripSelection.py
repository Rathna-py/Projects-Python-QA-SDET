import calendar
from utils.Loging import logger
from config.driver_manager import driver, close_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from flights_page import BasicConfig




# class SelectablePlace_Oneway_RoundTrip:
#
#     def from_departure_place(self, from_departure):
#         # From Place
#         from_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'fromCity')]")))
#         from_place.click()
#         time.sleep(2)
#
#         focus_from_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'react-autosuggest__input')]")))
#         focus_from_place.send_keys(from_departure)
#         time.sleep(2)
#
#         place_dropdown_list = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
#         place_dropdown_list.click()
#         logger.info("Successfully selected --- From --- place")
#
#
#     def to_departure_place(self, to_departure):
#         # To Place
#         to_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'toCity')]")))
#         to_place.click()
#         focus_to_place = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
#             (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
#         focus_to_place.send_keys(to_departure)
#         place_dropdown_list = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
#         place_dropdown_list.click()
#         time.sleep(5)
#         logger.info("Successfully selected  --- To  --- place")
#
#
# class Selectable_MultiCity:
#     def departure_from_place(self, fromCity1):
#         logger.info("Please Select From Cities: \nIf willing to add one more city, Please Enter 1")
#
#         # From Place City1
#         from_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'fromAnotherCity0')]")))
#         from_place.click()
#         time.sleep(2)
#
#         focus_from_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
#         focus_from_place.send_keys(fromCity1)
#         time.sleep(2)
#
#         place_dropdown_list = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
#         place_dropdown_list.click()
#         logger.info("Successfully selected --- From --- First place")

        # From Place City2
        # from_place = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'fromAnotherCity1')]")))
        # from_place.click()
        # time.sleep(2)
        #
        # focus_from_place = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
        # focus_from_place.send_keys(fromCity2)
        # time.sleep(2)
        #
        # place_dropdown_list = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
        # place_dropdown_list.click()
        # logger.info("Successfully selected --- From --- First place")


#     def AddCity(self, add_another_city, ToCity):
#         if add_another_city == 1:
#             add_city = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//button[contains(@data-cy,'addAnotherCity')]")))
#             add_city.click()
#
#             # From Place City1
#             to_place = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'toAnotherCity2')]")))
#             to_place.click()
#             time.sleep(2)
#
#             focus_to_place = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located(
#                     (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
#             focus_to_place.send_keys(ToCity)
#             time.sleep(2)
#
#             place_dropdown_list = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
#             place_dropdown_list.click()
#             logger.info("Successfully selected --- From --- First place")
#
#
#         else:
#             logger.info("No Add-on city option was selected")
#
#     def to_departure_place(self, ToCity1, ToCity2):
#         # To Place City1
#         to_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'toAnotherCity0')]")))
#         to_place.click()
#         time.sleep(2)
#
#         focus_to_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
#         focus_to_place.send_keys(ToCity1)
#         time.sleep(2)
#
#         place_dropdown_list = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
#         place_dropdown_list.click()
#         logger.info("Successfully selected --- From --- First place")
#
#         # To Place City2
#         to_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//label[contains(@for, 'toAnotherCity1')]")))
#         to_place.click()
#         time.sleep(2)
#
#         focus_to_place = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//input[contains(@class, 'react-autosuggest__input react-autosuggest__input--open')]")))
#         focus_to_place.send_keys(ToCity2)
#         time.sleep(2)
#
#         place_dropdown_list = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']")))
#         place_dropdown_list.click()
#         logger.info("Successfully selected --- From --- First place")
#
#
# class Selectable_Date:
#
#     def departure_date(self, depart_Date, depart_Month, depart_Year):
#         # Click on date selector/picker button
#         departure_selector = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
#             (By.XPATH, "//*[contains(@class, 'flt_fsw_inputBox dates inactiveWidget ')]")))
#         departure_selector.click()
#
#         # pick month and year
#         while True:
#             short_month = calendar.month_abbr[list(calendar.month_name).index(depart_Month)]
#             departure_target_date = f"{short_month} {depart_Date} {depart_Year}"
#             date_pick_container = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'DayPicker-Months')]"))).text
#             if depart_Month in date_pick_container and depart_Year in date_pick_container:
#                 pick_date = WebDriverWait(driver, 5).until(
#                     EC.presence_of_element_located(
#                         (By.XPATH, f"//div[contains(@aria-label, '{departure_target_date}')]")))
#                 pick_date.click()
#                 break
#
#             else:
#                 next_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
#                     (By.XPATH, "//*[contains(@class, 'DayPicker-NavButton DayPicker-NavButton--next')]")))
#                 next_button.click()
#                 time.sleep(3)
#         logger.info(f"Successfully selected Departure date")
#
#     def return_date(self, return_Date, return_Month, return_Year, departure_date):
#         return_target_date = f"{return_Date} {return_Month} {return_Year}"
#         if not BasicConfig.is_valid_date_range(departure_date, return_target_date):
#             logger.info("Invalid date range: Return date must be after departure date.")
#             return
#         # Click on date selector/picker button
#         departure_selector = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
#             (By.XPATH, "//*[contains(@class, 'flt_fsw_inputBox dates reDates inactiveWidget ')]")))
#         departure_selector.click()
#
#         # check return matches with departure date
#
#         # pick month and year
#         while True:
#             short_month = calendar.month_abbr[list(calendar.month_name).index(return_Date)]
#             return_target_date = f"{short_month} {return_Date} {return_Year}"
#             date_pick_container = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'DayPicker Selectable Range')]"))).text
#             if return_Month and return_Year in date_pick_container:
#                 pick_date = WebDriverWait(driver, 5).until(
#                     EC.presence_of_element_located((By.XPATH, f"//div[contains(@aria-label, '{return_target_date}')]")))
#                 pick_date.click()
#
#             else:
#                 next_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
#                     (By.XPATH, "//*[contains(@class, 'DayPicker-NavButton DayPicker-NavButton--next')]")))
#                 next_button.click()
#                 time.sleep(3)
#             logger.info(f"Successfully selected Return date")
