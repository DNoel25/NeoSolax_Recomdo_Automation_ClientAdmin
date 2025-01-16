# Pages/manual_suggestions_page.py
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators   
import logging
import time
from selenium.common.exceptions import TimeoutException

class SearchSortAndFilter:
    def __init__(self, driver):
        self.driver = driver
    
    def is_advanced_sortandfilter_heading_there(self): 
        try:
            heading1 = WebDriverWait(self.driver, 20).until(
                # EC.visibility_of_element_located((By.XPATH, "//h1[@class='text-5xl font-extrabold dark:text-white' and contains(., 'Search Result Advanced Sort & Filter')]"))
                EC.visibility_of_element_located((By.XPATH, "//h1[contains(@class, 'text-5xl') and contains(., 'Search Result Advanced Sort & Filter')]"))

            )
            print("Advanced Sort And Filter Heading is there")
            return heading1.is_displayed()
        except Exception as e:
            logging.error(f"Error locating Advanced Sort And Filter Heading: {e}")
            return False

    def select_storeview(self, store):
        # Select store view from dropdown
        store_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ASF_STORE_VIEW_DROPDOWN)
        )
        Select(store_dropdown).select_by_visible_text(store)
        print("Successfully selected the store view!")
    
    def select_sort_option_layered(self, sortOption):
        # Select store view from dropdown 
        sort_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ASF_SORTOPTION_LAYERED)
        )
        sort_option.click()
        Select(sort_option).select_by_visible_text(sortOption)
        
        print("Successfully Selected the Sort By Option in Layered Navigation Section!")

    def select_sort_option_layered1(self, sortOption):
        # Select store view from dropdown 
        sort_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ASF_SORTOPTION_LAYERED)
        )
        sort_option.click()
        Select(sort_option).select_by_visible_text(sortOption)
        
        print("Successfully Selected the Sort By Option in Layered Navigation Section!")

    def save_changes(self):
        """
        Click the save button on top right cornor.
        """
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ASF_SAVE_BUTTON)
        )
        save_button.click()
    

    def search_in_unassign_box(self, search_text):
        try:
            # Locate and clear the unassigned search field, then enter the search text
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.ASF_SEARCH_TEXT)  # Assuming Locators.ASF_SEARCH_TEXT is By.ID("search_unassigned")
            )
            search_field.clear()
            search_field.send_keys(search_text)
            print(f"Searching for '{search_text}' in the unassigned attributes box...")

            # Wait for the search results to update in the unassigned list
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sortable-list.unassigned-list .unassigned_attribute_one"))  # Assuming Locators.ASF_UNASSIGNED_LIST is By.CSS_SELECTOR
            )

            # Fetch all filtered items in the unassigned list
            items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.unassigned-list .unassigned_attribute_one")
            print(f"Got {len(items)} filtered items in the unassigned attributes list.")

            # Verify if the searched text appears in any item of the unassigned list
            for item in items:
                try:
                    # Find the span containing the attribute name within the current item
                    attribute_name_span = item.find_element(By.CLASS_NAME, "attribute_name")
                    item_text = attribute_name_span.text.strip()  # Extract text from the span

                    if search_text.lower() in item_text.lower():  # Partial case-insensitive match
                        print(f"Match found: '{search_text}' in unassigned attribute: '{item_text}'")
                        time.sleep(5)
                        return True  # Return True if a match is found

                except Exception as e:
                    logging.error(f"Error processing item: {e}")
                    continue

            print(f"'{search_text}' not found in the unassigned attributes list.")


        except Exception as e:
            logging.error(f"Error during search in unassigned attributes box: {e}")
            return False  

    def enter_15_in_searched_field(self, search_text):
        try:
            # Locate the input field for the searched attribute (e.g., 'Age')
            input_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 
                    f"li[id='{search_text}'] .number_div input[name='order_number_unassigned']"
                ))
            )
            
            # Clear the input field and type '16'
            input_field.clear()
            input_field.send_keys("15")
            print(f"Entered '15' in the searched field for '{search_text}'.")
            time.sleep(2)
            return True  # Successfully entered '16' in the field

        except Exception as e:
            logging.error(f"Error during entering '16' in the searched field for '{search_text}': {e}")
            return False  # If an error occurs, return False


    def search_in_assign_box(self, search_text):
        try:    
        #############################
            # If not found in unassigned list, search in assigned attributes list
            print(f"Searching for '{search_text}' in the assigned attributes list...")
            assigned_search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "search_assigned"))  # ID for the assigned search field
            )
            assigned_search_field.clear()
            assigned_search_field.send_keys(search_text)

            # Wait for the search results to update in the assigned list
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sortable-list.assigned-list .assigned_attribute_one"))
            )

            # Fetch all filtered items in the assigned list
            assigned_items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.assigned-list .assigned_attribute_one")
            print(f"Got {len(assigned_items)} filtered items in the assigned attributes list.")

            # Verify if the searched text appears in any item of the assigned list
            for assigned_item in assigned_items:
                try:
                    # Find the span containing the attribute name within the current item
                    attribute_name_span = assigned_item.find_element(By.CLASS_NAME, "attribute_name")
                    assigned_item_text = attribute_name_span.text.strip()  # Extract text from the span

                    if search_text.lower() in assigned_item_text.lower():  # Partial case-insensitive match
                        print(f"Match found: '{search_text}' in assigned attribute: '{assigned_item_text}'")
                        time.sleep(5)
                        return True  # Return True if a match is found

                except Exception as e:
                    logging.error(f"Error processing assigned item: {e}")
                    continue

            print(f"'{search_text}' not found in the assigned attributes list.")
            return False  # Return False if no match is found in both lists


        except Exception as e:
            logging.error(f"Error during search in unassigned attributes box: {e}")
            return False
    
    def enter_1_in_searched_field(self, search_text):
        try:
            # Fetch all filtered items in the assigned list
            assigned_items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.assigned-list .assigned_attribute_one")
            print(f"Got {len(assigned_items)} filtered items in the assigned attributes listsss.")

            if (len(assigned_items)) > 1:
                # Locate the input field for the searched attribute (e.g., 'Age')
                input_field1 = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((
                        By.CSS_SELECTOR, 
                        f"li[id='{search_text}'] .number_div input[name='order_number_assigned']"
                    ))
                )
                
                # Clear the input field and type '1'
                input_field1.clear()
                input_field1.send_keys("1")
                print(f"Entered '1' in the searched field for '{search_text}'.")
                time.sleep(2)

                #Saving the changes
                self.save_changes() 
            
                # Optional: Wait for the page to refresh or changes to take effect
                WebDriverWait(self.driver, 10).until(EC.staleness_of(input_field1)) 
                # Step 4: Verify the updated value in the input field
                updated_input_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 
                        f"li[id='{search_text}'] .number_div input[name='order_number_assigned']"
                    ))
                )
  
                # Step 5: Retrieve the value and check if it is updated to '1'
                input_value = updated_input_field.get_attribute('value')
                if input_value == "1":
                    print("The keyword has been updated to 1 successfully.")
                else:
                    print(f"The keyword update failed. Current value: {input_value}")
                
            else:
                print("huhuhu not greater")
            
        except Exception as e:
            logging.error(f"Error during entering '16' in the searched field for '{search_text}': {e}")
            return False  # If an error occurs, return False

    def is_delete_button_visible_for_price(self):
        """
        Check if the delete button is visible for the 'Price' attribute in the assigned list.
        :return: True if the delete button is visible, False otherwise.
        """
        try:
            # Wait for the specific 'Price' attribute element in the assigned list
            price_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//li[@class='assigned_attribute_one' and @id='price']")
                )
            )
            print("Found the 'Price' attribute in the assigned list.")

            # Check if the delete button exists within this element
            delete_button = price_element.find_elements(By.CSS_SELECTOR, "button.delete-button")
            if not delete_button:
                print("Delete button is NOT visible for 'Price', as expected.")
                return True  # Delete button is visible
            else:
                print("Delete button is visible for 'Price'. This is unexpected.")
                return False  # Delete button is not visible
        except TimeoutException:
            print("Timed out waiting for the 'Price' attribute to load.")
            return False
        except NoSuchElementException as e:
            print(f"Error locating 'Price' attribute or its delete button: {e}")
            return False
    
    #STARTING THE TEST on SORT BY OPTION FILTER
    #******************************************
    def select_sort_option_sortby(self, sortOption):
        # Select store view from dropdown 
        sort_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ASF_SORTOPTION_SORTBY)
        )
        sort_option.click()
        Select(sort_option).select_by_visible_text(sortOption)
        
        print("Successfully Selected the Sort By Option in Sort By Section!")

    def search_in_sortby_unassign_box(self, search_text):
        try:
            # Locate and clear the unassigned search field, then enter the search text
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.ASF_SEARCH_TEXT)  # Assuming Locators.ASF_SEARCH_TEXT is By.ID("search_unassigned")
            )
            search_field.clear()
            search_field.send_keys(search_text)
            print(f"Searching for '{search_text}' in the unassigned attributes box...")

            # Wait for the search results to update in the unassigned list
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sortable-list.unassigned-list .unassigned_attribute_one"))  # Assuming Locators.ASF_UNASSIGNED_LIST is By.CSS_SELECTOR
            )

            # Fetch all filtered items in the unassigned list
            items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.unassigned-list .unassigned_attribute_one")
            print(f"Got {len(items)} filtered items in the unassigned attributes list.")

            # Verify if the searched text appears in any item of the unassigned list
            for item in items:
                try:
                    # Find the span containing the attribute name within the current item
                    attribute_name_span = item.find_element(By.CLASS_NAME, "attribute_name")
                    item_text = attribute_name_span.text.strip()  # Extract text from the span

                    if search_text.lower() in item_text.lower():  # Partial case-insensitive match
                        print(f"Match found: '{search_text}' in unassigned attribute: '{item_text}'")
                        time.sleep(5)
                        return True  # Return True if a match is found

                except Exception as e:
                    logging.error(f"Error processing item: {e}")
                    continue

            print(f"'{search_text}' not found in the unassigned attributes list.")


        except Exception as e:
            logging.error(f"Error during search in unassigned attributes box: {e}")
            return False  

    def enter_15_in_sortby_searched_field(self, search_text):
        try:
            # Locate the input field for the searched attribute (e.g., 'Age')
            # input_field = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((
            #         By.CSS_SELECTOR, 
            #         f"li[id='{search_text}'] .number_div input[name='order_number_unassigned']"
            #     ))
            # )
            print("heheheheheheh")
            print("Here is the problemmmmmmmmmmmmmmmmmm......")
            input_field = WebDriverWait(self.driver, 10).until(
                
                EC.visibility_of_element_located((
                        By.CSS_SELECTOR,
                        f"div.number_div span input.order_number_unassigned[name='order_number_unassigned'][type='number'] + span[data-code='{search_text}']"
                    ))
            )
            print("ahahahahah2222222")
            # Clear the input field and type '16'
            input_field.clear()
            input_field.send_keys("15") 
            print(f"Entered '15' in the searched field for '{search_text}'.")
            time.sleep(2)
            return True  # Successfully entered '16' in the field

        except Exception as e:
            logging.error(f"Error during entering '16' in the searched field for '{search_text}': {e}")
            return False  # If an error occurs, return False


    def search_in_sortby_assign_box(self, search_text):
        try:    
        #############################
            # If not found in unassigned list, search in assigned attributes list
            print(f"Searching for '{search_text}' in the assigned attributes list...")
            assigned_search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "search_sortunassigned"))  # ID for the assigned search field
            )
            assigned_search_field.clear()
            assigned_search_field.send_keys(search_text)

            # Wait for the search results to update in the assigned list
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sortable-list.sort_unassigned-list"))
            )

            # Fetch all filtered items in the assigned list
            assigned_items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.sort_unassigned-list li")
            print(f"Got {len(assigned_items)} filtered items in the assigned attributes list.")

            # Verify if the searched text appears in any item of the assigned list
            for assigned_item in assigned_items:
                try:
                    # Find the span containing the attribute name within the current item
                    attribute_name_span = assigned_item.find_element(By.CLASS_NAME, "attribute_name")
                    assigned_item_text = attribute_name_span.text.strip()  # Extract text from the span

                    if search_text.lower() in assigned_item_text.lower():  # Partial case-insensitive match
                        print(f"Match found: '{search_text}' in assigned attribute: '{assigned_item_text}'")
                        time.sleep(5)
                        return True  # Return True if a match is found

                except Exception as e:
                    logging.error(f"Error processing assigned item: {e}")
                    continue

            print(f"'{search_text}' not found in the assigned attributes list.")
            return False  # Return False if no match is found in both lists


        except Exception as e:
            logging.error(f"Error during search in unassigned attributes box: {e}")
            return False
    
    def enter_1_in_sortby_searched_field(self, search_text):
        try:
            # Fetch all filtered items in the assigned list
            assigned_items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.assigned-list .assigned_attribute_one")
            print(f"Got {len(assigned_items)} filtered items in the assigned attributes listsss.")

            if (len(assigned_items)) > 1:
                # Locate the input field for the searched attribute (e.g., 'Age')
                input_field1 = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((
                        By.CSS_SELECTOR, 
                        f"li[id='{search_text}'] .number_div input[name='order_number_assigned']"
                    ))
                )
                
                # Clear the input field and type '1'
                input_field1.clear()
                input_field1.send_keys("1")
                print(f"Entered '1' in the searched field for '{search_text}'.")
                time.sleep(2)

                #Saving the changes
                self.save_changes() 

                # Optional: Wait for the page to refresh or changes to take effect
                WebDriverWait(self.driver, 10).until(EC.staleness_of(input_field1)) 
                # Step 4: Verify the updated value in the input field
                updated_input_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 
                        f"li[id='{search_text}'] .number_div input[name='order_number_assigned']"
                    ))
                )
  
                # Step 5: Retrieve the value and check if it is updated to '1'
                input_value = updated_input_field.get_attribute('value')
                if input_value == "1":
                    print("The keyword has been updated to 1 successfully.")
                else:
                    print(f"The keyword update failed. Current value: {input_value}")
                
            else:
                print("huhuhu not greater")
            
        except Exception as e:
            logging.error(f"Error during entering '16' in the searched field for '{search_text}': {e}")
            return False  # If an error occurs, return False
