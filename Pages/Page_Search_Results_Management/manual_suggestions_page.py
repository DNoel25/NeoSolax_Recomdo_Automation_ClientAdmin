# Pages/manual_suggestions_page.py
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators   
import logging
import time


class ManualSuggestionsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def is_manual_suggestion_heading_there(self): 
        try:
            heading = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@class='text-5xl font-extrabold dark:text-white' and contains(., 'Manual Suggestions')]"))
            )
            print("Manual Suggestion Heading is there")
            return heading.is_displayed()
        except Exception as e:
            logging.error(f"Error locating Manual Suggestion heading: {e}")
            return False


    def is_grid_displayed(self):
        try:
            grid = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//table[@id='SuggestionTable']"))
            )
            print("Manual Suggestion grid is there")
            return grid.is_displayed()
        except Exception as e:
            logging.error(f"Error locating grid element: {e}")
            return False


    def set_show_entries(self, value):
        try:
            print(f"Setting show entries to {value}")
            
            # Locate the dropdown element and create a Select object
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.SHOW_ENTRIES_DROPDOWN)
            )
            select = Select(dropdown_element)
            
            # Select the desired option in the dropdown
            select.select_by_visible_text(str(value))
            print(f"Dropdown set to {value}")

            # Wait until the grid is updated by checking the number of rows
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(By.XPATH, "//table[@id='SuggestionTable']/tbody/tr")) <= int(value)
            )
            
            # Fetch the updated rows after setting the dropdown
            rows = self.driver.find_elements(By.XPATH, "//table[@id='SuggestionTable']/tbody/tr")
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
                EC.visibility_of_element_located((By.XPATH, "//input[@aria-controls='SuggestionTable']"))
            )
            search_field.clear()
            search_field.send_keys(text)
            print(f"Searching for '{text}' in the grid...")

            # Wait for the search results to be displayed in the grid
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//table[@id='SuggestionTable']/tbody/tr"))
            )

            # Fetch all rows in the grid
            rows = self.driver.find_elements(By.XPATH, "//table[@id='SuggestionTable']/tbody/tr")

            # Check if any cell in any row contains the search text
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                for cell in cells:
                    if text.lower() in cell.text.lower():  # Case-insensitive match
                        print(f"Found '{text}' in grid cell with text: '{cell.text}'")
                        return True  # Return True if a match is found
            print(f"No match found for '{text}' in the grid.")
            return False  # Return False if no match is found in any cell

        except Exception as e:
            logging.error(f"Error during search in grid: {e}")
            return False
    #All the add new Page Handlings
    def click_add_new(self):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ADD_NEW_BUTTON)
        )
        add_button.click()
   
    def fill_form(self, store, keyword, synonyms, weights):
        # Select store view from dropdown
        store_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.STORE_VIEW_DROPDOWN)
        )
        Select(store_dropdown).select_by_visible_text(store)

        # Fill the keyword field
        keyword_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.KEYWORD_FIELD)
        )
        keyword_field.clear()
        keyword_field.send_keys(keyword)

        # Fill synonyms and weights fields
        synonym_fields = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(Locators.SYNONYM_FIELD)
        )
        weight_fields = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(Locators.WEIGHT_FIELD)
        )

        # Ensure we only loop through available fields up to a maximum of three
        max_entries = min(3, len(synonym_fields), len(weight_fields))
        for i in range(max_entries):
            synonym_fields[i].clear()
            synonym_fields[i].send_keys(synonyms[i])

            weight_fields[i].clear()
            weight_fields[i].send_keys(str(weights[i]))  # Convert weight to string

    def submit_form(self):
        # Click the save button
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SAVE_BUTTON)
        )
        save_button.click()


    #All the edit process in the Page Handling
    def click_edit_button(self, search_keyword, row_index=0):
        """
        Clicks the edit button for a specific row in the grid after searching for a keyword.
        """
        self.search_in_grid(search_keyword)
        edit_buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(Locators.EDIT_BUTTON)
        )
        assert edit_buttons, "No edit buttons found in the grid."
        edit_buttons[row_index].click()

    def edit_synonym(self, synonym_index, new_synonym):
        """
        Edit a specific synonym in the edit form.
        """
        synonym_fields = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(Locators.SYNONYM_FIELD)
        )
        assert len(synonym_fields) > synonym_index, f"Synonym field at index {synonym_index} not found."
        synonym_fields[synonym_index].clear()
        synonym_fields[synonym_index].send_keys(new_synonym)

    def save_changes(self):
        """
        Click the save button on the edit form.
        """
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SAVE_BUTTON)
        )
        save_button.click()  

    def verify_updated_suggestion(self, keyword, expected_synonym):
        # Locate and clear the search field, then enter the search text
        search_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@aria-controls='SuggestionTable']"))
        )
        search_field.clear()
        search_field.send_keys(keyword)
        print(f"Searching for '{keyword}' in the grid...")

        # Wait for the search results to be displayed in the grid
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//table[@id='SuggestionTable']/tbody/tr"))
        )
        
        # Locate the suggestion column for the first row
        suggestion_cell = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//table[@id='SuggestionTable']/tbody/tr[1]/td[4]"))  # Update the XPATH as needed
        )
        
        # Extract the displayed text
        actual_suggestion = suggestion_cell.text.strip()
        print(f"Grid cell text found: {actual_suggestion}")
        time.sleep(2)
        # Assert that the updated synonym is present
        assert expected_synonym in actual_suggestion, f"Expected synonym '{expected_synonym}' not found in grid. Found: '{actual_suggestion}'"
        print(f"Updated synonym '{expected_synonym}' verified successfully!")


    # def click_delete_button(self, keyword):
    #     try:
    #         # Search the keyword
    #         self.search_in_grid(keyword) 
    #         # wait to load the filtered searched
    #         rows = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, "//table[@id='SuggestionTable']/tbody/tr"))
    #         ) 
            
    #         # Ensure at least one matching record exists
    #         if not rows:
    #             print(f"No records found for keyword '{keyword}' to delete.")
    #             return False
    
    #         # Wait until the table's first row delete button is clickable, and click it
    #         delete_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//table[@id='SuggestionTable']/tbody/tr[1]//i[contains(@class, 'delete-item')]"))
    #         )
    #         delete_button.click()

    #         # Verify the confirmation delete btn
    #         confirm_btn = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm_delete_button']"))
    #         )
    #         confirm_btn.click()
    #         print("Searched TopMost row is deleted succussfully") 
            
    #         # # Wait until the success message is visible
    #         # success_message = WebDriverWait(self.driver, 20).until(
    #         #     EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible' and contains(text(), 'Suggestion deleted successfully!')]"))
    #         # )

    #         # # Verify the success message text
    #         # assert "Suggestion deleted successfully!" in success_message.text, "Success message not displayed or incorrect."
    #         # print("Success message displayed: 'Suggestion deleted successfully!'")


    #         self.search_in_grid(keyword)
    #         updated_rows = self.driver.find_elements(By.XPATH, "//table[@id='SuggestionTable']/tbody/tr")

    #         assert len(updated_rows) <len(rows), f"Top record with keyword '{keyword}' was not deleted."
    #         print(f"Top record with keyword '{keyword}' successfully deleted.")

    #     except Exception as e:
    #         logging.error(f"Error deleting top record with keyword '{keyword}': {e}")
    #         return False