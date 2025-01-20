from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators   
from Pages.sidebar_page import SideNavigationPage
import logging
import time
from selenium.webdriver.common.keys import Keys

class SearchTermPages:
    def __init__(self, driver):
        self.driver = driver
        # Define the frame locator
        self.frame_locator = (By.CSS_SELECTOR, "iframe.note-editor.note-frame")  # Adjust this if necessary
        # Define the contenteditable div locator
        self.editable_div_locator = (By.CSS_SELECTOR, "div.note-editable[contenteditable='true']")
    
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
            logging.error(f"Error locating Search Term Pages Heading: {e}")
            return False

    def is_grid_displayed(self):
        try:
            grid = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//table[@id='allPageTable']"))
            )
            print("Search Term Pages page grid is there")
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
                EC.element_to_be_clickable(Locators.STAP_SHOW_ENTRIES_DROPDOWN)
            )
            select = Select(dropdown_element)
            
            # Select the desired option in the dropdown
            select.select_by_visible_text(str(value))
            print(f"Dropdown set to {value}")

            # Wait until the grid is updated by checking the number of rows
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(By.XPATH, "//table[@id='allPageTable']/tbody/tr")) <= int(value)
            )
            
            # Fetch the updated rows after setting the dropdown
            rows = self.driver.find_elements(By.XPATH, "//table[@id='allPageTable']/tbody/tr")
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
                EC.visibility_of_element_located((By.XPATH, "//input[@aria-controls='allPageTable']"))
            ) 
            search_field.clear()
            search_field.send_keys(text)
            print(f"Searching for '{text}' in the grid...")

            # Wait for the search results to be displayed in the grid
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//table[@id='allPageTable']/tbody/tr"))
            )
            time.sleep(2)
            # Fetch all rows in the grid
            rows = self.driver.find_elements(By.XPATH, "//table[@id='allPageTable']/tbody/tr")

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
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(Locators.STAP_PAGINATION_CONTAINER)
        )

    def no_of_rows(self):
        try:
            # Wait for the search results to be displayed in the grid
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//table[@id='allPageTable']/tbody/tr"))
            )
            time.sleep(2)
            # Fetch all rows in the grid
            rows = self.driver.find_elements(By.XPATH, "//table[@id='allPageTable']/tbody/tr")

            # Check if the number of rows is greater than 10
            if len(rows) > 10:
                return True
            else:
                print(f"Number of rows is {len(rows)}, which is not greater than 10 So the pagination testing will not be there.")
                return False
        except Exception as e:
            print(f"The error is: {e}")
            return False

    def get_active_page(self):
        active_page = self.driver.find_element(By.CSS_SELECTOR, ".paginate_button.current")
        return int(active_page.text)

    def click_next(self):
        next_btn = self.driver.find_element(*Locators.STAP_NEXT_BUTTON)
        next_btn.click()
        time.sleep(2)  # Wait for the new data to load

    def click_previous(self):
        prev_btn = self.driver.find_element(*Locators.STAP_PREVIOUS_BUTTON)
        prev_btn.click()
        time.sleep(2)  # Wait for the new data to load

    def click_page_number(self, page_number):
        pages = self.driver.find_elements(*Locators.STAP_PAGE_NUMBERS)
        for page in pages:
            if page.text == str(page_number):
                page.click()
                time.sleep(2)  # Wait for the new data to load
                break

    def get_last_page_number(self):
        """
        Retrieve the number of the last page in the pagination.
        """
        last_page_element = self.driver.find_element(*Locators.STAP_LAST_PAGE_NUMBER)
        last_page_text = last_page_element.text.strip()
        try:
            return int(last_page_text)
        except ValueError:
            raise ValueError(f"Unexpected non-numeric value found for last page number: {last_page_text}")

    def is_previous_disabled(self):
        return "disabled" in self.driver.find_element(*Locators.STAP_PREVIOUS_BUTTON).get_attribute("class")

    def is_next_disabled(self):
        return "disabled" in self.driver.find_element(*Locators.STAP_NEXT_BUTTON).get_attribute("class")

    def go_to_dashboard(self): 
        side_nav = SideNavigationPage(self.driver) 
        side_nav = side_nav.open_dashboard_menu()
        time.sleep(2)

#Testing create new scenario
    
    def go_to_addnew_form(self):
        # Locate and clear the search field, then enter the search text
        addnew_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ST_CREATE_NEW_BUTTON)
        )
        addnew_button.click()
        time.sleep(2)

    def fill_general(self, title, keyword, store_value):
        print("1")
        # Enable SEO Page
        # checkbox = self.driver.find_element(*Locators.STCN_ENABLE_SEO_CHECKBOX) 
        # if not checkbox.is_selected():
        #     checkbox.click()
        # Click the checkbox via label or JavaScript
        active = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "is_active"))
        )
        if active.is_selected():
            active.click()
        #Fill title
        title_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="category_name"]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", title_element)
        title_element.clear()
        title_element.send_keys({title})
        #Fill keyword
        keyword_element = (self.driver.find_element(By.XPATH, '//*[@id="search_keyword"]'))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", keyword_element)
        keyword_element.clear()
        keyword_element.send_keys(keyword)
        store_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.STCN_STORE_VIEW_DROPDOWN)
        )

        # Ensure the dropdown is scrolled into view
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                   store_dropdown)

        # Click to open the dropdown
        store_dropdown.click()

        try:
            # Wait for the option with the value attribute to be clickable
            option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//option[@value='{store_value}']"))
            )

            # Click the option
            option.click()

        except TimeoutException:
            print(f"Timeout: Could not find or click the option with value '{store_value}'.")
            # You can also add more debugging information here if needed
            # Use JavaScript to click the element if it's not clickable
            self.driver.execute_script(f"arguments[0].querySelector('option[value=\"{store_value}\"]').click();",
                                       store_dropdown)
        print("5")
        time.sleep(5)

        content_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_page_create"]/div/ul/li[2]/a'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                   content_tab)
        content_tab.click()
        time.sleep(2)
        print("Filled the general details and moved to content tab successfuly..")

    #all the upload image in content realted
    # Locators
    upload_button_locator = (By.ID, "upload_btn")
    file_input_locator = (By.ID, "file_input")
    preview_image_locator = (By.ID, "preview_image")
    file_details_locator = (By.ID, "file_details")
    delete_button_locator = (By.ID, "action-remove")


    def upload_image(self, file_path):
        """
        Uploads an image file using the file input element.

        :param file_path: The absolute path of the image file to upload.
            """
        file_input = self.driver.find_element(*self.file_input_locator)
        file_input.send_keys(file_path)
        time.sleep(3)

    def is_preview_image_displayed(self):
        """
        Checks if the preview image is displayed after upload.

        :return: True if the preview image is displayed, False otherwise.
        """
        preview_image = self.driver.find_element(*self.preview_image_locator)
        time.sleep(3)
        return preview_image.get_attribute("src") != ""

    def get_file_details(self):
        """
        Retrieves the file details displayed after uploading the image.

        :return: The text content of the file details element.
        """
        file_details = self.driver.find_element(*self.file_details_locator)
        time.sleep(3)
        return file_details.text

    def delete_image(self):

        self.driver.save_screenshot("debug_screenshot.png")
        """
        Deletes the uploaded image using the delete button.
        """
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_button_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", delete_button)
        delete_button.click()

    #all the content description realed functions
    def switch_to_note_frame(self):
        """
        Switches the WebDriver's context to the note-editor iframe.
        """
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(self.frame_locator)
        )

    def enter_description(self, description_text):
        """
        Enters the description text inside the note-editor contenteditable div.

        :param description_text: Text to be entered inside the editor.
        """
        # Wait for the contenteditable div to be present
        editable_div = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.editable_div_locator)
        )
        # Clear any existing text
        self.driver.execute_script("arguments[0].innerHTML = '';", editable_div)
        # Enter new text
        editable_div.send_keys(description_text)

    def switch_to_default_content(self):
        """
        Switches the WebDriver's context back to the default content.
        """
        self.driver.switch_to.default_content()


    # def is_image_deleted(self):
    #     """
    #     Checks if the preview image has been removed after clicking delete.
    #
    #     :return: True if the preview image is not displayed, False otherwise.
    #     """
    #     time.sleep(2)  # Wait for the deletion process to complete
    #     preview_image = self.driver.find_element(*self.preview_image_locator)
    #     return preview_image.get_attribute("src") == ""


    def fill_seo_fields(self):
        seo_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_page_create"]/div/ul/li[4]/a'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                   seo_tab)
        seo_tab.click()
        time.sleep(2)

        metatitle  = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'meta_title'))
        )
        metatitle.clear()
        metatitle.send_keys("test automation metat title")

        metkeywords = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'meta_keywords'))
        )
        metkeywords.clear()
        metkeywords.send_keys("test automation metat title")

        metacontent = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'meta_content'))
        )
        metacontent.clear()
        metacontent.send_keys("test automation metat title")

        metadescription = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'meta_description'))
        )
        metadescription.clear()
        metadescription.send_keys("test automation metat title")
        print("Successfully filled the SEO fields")

    # def fill_
