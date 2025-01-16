from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators   
from Pages.sidebar_page import SideNavigationPage
import logging
import time

class SearchTermPages:
    def __init__(self, driver):
        self.driver = driver
    
    def is_search_term_pages_heading_there(self):
        time.sleep(5) 
        try: 
            heading = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@class='text-5xl font-extrabold dark:text-white' and contains(., 'Search Term Pages')]"))
            )
            print("Search Term Pages Heading is there")
            time.sleep(2)
            return heading.is_displayed()
        
        except Exception as e:
            logging.error(f"Error locating Search Term Pages heading: {e}")
            return False

    def is_grid_displayed(self):
        try:
            grid = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//table[@id='seoSearchCountTable']"))
            )
            print("Search Term Pages grid is there")
            return grid.is_displayed()
        
        except Exception as e:
            logging.error(f"Error locating grid element: {e}")
            return false

    def set_show_entries(self, value):
        time.sleep(5)
        try:
            print(f"Setting show entries to {value}")
            
            # Locate the dropdown element and create a Select object
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.RMSTP_SHOW_ENTRIES_DROPDOWN)
            )
            select = Select(dropdown_element)
            
            # Select the desired option in the dropdown
            select.select_by_visible_text(str(value))
            print(f"Dropdown set to {value}")

            # Wait until the grid is updated by checking the number of rows
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(By.XPATH, "//table[@id='seoSearchCountTable']/tbody/tr")) <= int(value)
            )
            
            # Fetch the updated rows after setting the dropdown
            rows = self.driver.find_elements(By.XPATH, "//table[@id='seoSearchCountTable']/tbody/tr")
            actual_count = len(rows)
            
            # Debug print to confirm actual count
            print(f"Expected up to {value} entries, found {actual_count} entries in the grid.")

            # Verify if the number of rows is equal to the selected dropdown value or less
            assert actual_count == int(value) or actual_count < int(value), f"Expected up to {value} entries, but found {actual_count}."
            
        except Exception as e:
            logging.error(f"Error in setting show entries dropdown: {e}")
            return False
        return True

    def search_in_grid(self, text): 
        try:
            # Locate and clear the search field, then enter the search text
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@aria-controls='seoSearchCountTable']"))
            ) 
            search_field.clear()
            search_field.send_keys(text)
            print(f"Searching for '{text}' in the grid...")

            # Wait for the search results to be displayed in the grid
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//table[@id='seoSearchCountTable']/tbody/tr"))
            ) 
            time.sleep(2)
            # Fetch all rows in the grid
            rows = self.driver.find_elements(By.XPATH, "//table[@id='seoSearchCountTable']/tbody/tr")

            # Check if any cell in any row contains the search text
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                for cell in cells:
                    if text.lower() in cell.text.lower():  # Case-insensitive match
                        print(f"Found '{text}' in grid cell with text: '{cell.text}'")
                        time.sleep(2)
                        search_field.clear()
                        self.driver.refresh()
                        time.sleep(2)
                        return True  # Return True if a match is found
            print(f"No match found for '{text}' in the grid.")
            return False  # Return False if no match is found in any cell

        except Exception as e:
            logging.error(f"Error during search in grid: {e}")
            return False

    #followings are the paginations testing
    def wait_for_pagination(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.RMSTP_PAGINATION_CONTAINER)
        )

    def get_active_page(self):
        active_page = self.driver.find_element(By.CSS_SELECTOR, ".paginate_button.current")
        return int(active_page.text)

    def click_next(self):
        next_btn = self.driver.find_element(*Locators.RMSTP_NEXT_BUTTON)
        next_btn.click()
        time.sleep(2)  # Wait for the new data to load

    def click_previous(self):
        prev_btn = self.driver.find_element(*Locators.RMSTP_PREVIOUS_BUTTON)
        prev_btn.click()
        time.sleep(2)  # Wait for the new data to load

    def click_page_number(self, page_number):
        pages = self.driver.find_elements(*Locators.RMSTP_PAGE_NUMBERS)
        for page in pages:
            if page.text == str(page_number):
                page.click()
                time.sleep(2)  # Wait for the new data to load
                break

    def get_last_page_number(self):
        """
        Retrieve the number of the last page in the pagination.
        """
        last_page_element = self.driver.find_element(*Locators.RMSTP_LAST_PAGE_NUMBER)
        last_page_text = last_page_element.text.strip()
        try:
            return int(last_page_text)
        except ValueError:
            raise ValueError(f"Unexpected non-numeric value found for last page number: {last_page_text}")

    def is_previous_disabled(self):
        return "disabled" in self.driver.find_element(*Locators.RMSTP_PREVIOUS_BUTTON).get_attribute("class")

    def is_next_disabled(self):
        return "disabled" in self.driver.find_element(*Locators.RMSTP_NEXT_BUTTON).get_attribute("class")

    def go_to_dashboard(self): 
        side_nav = SideNavigationPage(self.driver) 
        side_nav = side_nav.open_dashboard_menu()
        time.sleep(2)

        