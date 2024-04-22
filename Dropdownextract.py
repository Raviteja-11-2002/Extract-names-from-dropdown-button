import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_survey_numbers(district, mandal, village):
    chromedriver_autoinstaller.install()

    # Create a new Chrome browser instance
    driver = webdriver.Chrome()

    # Navigate to the webpage
    driver.get("https://dharani.telangana.gov.in/knowLandStatus")

    # Wait for the district dropdown to be clickable
    district_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "districtID"))
    )

    # Select the district
    district_dropdown.send_keys(district)

    # Wait for a short delay to allow the options to load
    time.sleep(2)

    # Wait for the mandal dropdown to be clickable
    mandal_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mandalID"))
    )

    # Select the mandal
    mandal_dropdown.send_keys(mandal)

    # Wait for a short delay to allow the options to load
    time.sleep(2)

    # Wait for the village dropdown to be clickable
    village_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "villageId"))
    )

    # Select the village
    village_dropdown.send_keys(village)

    # Wait for a short delay to allow the options to load
    time.sleep(2)

    # Wait for the survey number dropdown to be clickable
    survey_number_dropdown = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.ID, "surveyheader"))
    )

    # Print debugging information
    print("Survey number dropdown is clickable")

    # Wait for the survey number options to load
    survey_number_options = WebDriverWait(survey_number_dropdown, 100).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "option"))
    )

    # Print debugging information
    print(f"{len(survey_number_options)} survey number options are present")

    # Extract the survey numbers
    survey_numbers = [option.get_attribute("value") for option in survey_number_options if option.get_attribute("value")]

    # Close the browser
    driver.quit()

    return survey_numbers

if __name__ == "__main__":
    district = "Nagarkurnool"
    mandal = "Veldanda"
    village = "Ajilapur"

    survey_numbers = get_survey_numbers(district, mandal, village)
    print(f"Survey numbers for {district}, {mandal}, and {village}:")
    print(survey_numbers)