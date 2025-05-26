# MakeMyTrip_Flights POM

```
# POM_MakeMyTrip

```
## Project Overview
This project automates the process of booking flights on the MakeMyTrip portal using Selenium WebDriver in Python. The script handles various aspects of the booking process,
 including selecting trip types, choosing departure and arrival locations, setting travel dates, and selecting the number of travelers and travel class.

```
## Directory Structure
```POM_MakeMyTrip/
│
├── .venv/
│
├── config/
│
├── pages/
│   ├── FlightBooking/
│   │   ├── Logs/
│   │   │   ├── __init__.py
│   │   │   ├── flights_page.py
│   │   │   └── TripSelection.py
│   ├── Logs/
│   │   ├── __init__.py
│
├── tests/
│   ├── conftest.py
│
├── utils/
│   ├── Loging.py```
```

## Prerequisites

- Python 3.x
- Selenium
- Chrome WebDriver
- WebDriver Manager

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rrakshithaa/POM_MakeMyTrip.git
   cd POM_MakeMyTrip/POM_Flightbooking
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have Chrome WebDriver installed:**
   ```bash
   pip install webdriver-manager
   ```

## Usage

1. **Run the script:**
   ```bash
   python flights_page\ 2.py
   ```

2. **Script functionalities:**
   - **Close login panel:** Automatically closes the login panel if it appears.
   - **Select trip type:** Choose between one-way, round-trip, or multi-city trips.
   - **Select departure and arrival locations:** Specify the cities for departure and arrival.
   - **Set travel dates:** Choose the departure and return dates.
   - **Select travelers and class:** Specify the number of adults, children, infants, and the travel class (Economy, Premium Economy, Business, First Class).
   - **Special fare options:** Choose special fare options like Regular, Student, Senior Citizen, Armed Forces, Doctor, and Nurse.

## Example

Here's an example of how to use the script to book a round-trip flight:

```python
if __name__ == '__main__':
    driver.get("https://www.makemytrip.com/flights/")
    logger.info("Opening the link")
    driver.maximize_window()
    time.sleep(5)
    basic_config = BasicConfig()
    basic_config.close_login_panel()
    select_trip = Select_trip()
    select_trip.select_trip_type('roundtrip')
```

## Logging

The script uses a logging module to log important events and errors. Ensure you have the `utils.Loging` module configured correctly.

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.
