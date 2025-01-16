# Tests/test_layered_navigation.py
import logging
import time
import pytest
from Pages.sidebar_page import SideNavigationPage
from Pages.Page_Category_Management.layered_navigation_page import LayeredNavigationPage
from Utils.base import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# @pytest.mark.usefixtures("setup")
class TestCategoryManagement(BaseTest):

    try:
        @classmethod
        def setup_class(cls):
            super().setup_class()
            side_nav = SideNavigationPage(cls.driver)
            side_nav.open_category_management()
            side_nav.open_layered_navigation()

        # @pytest.mark.order(1)
        # def test_heading_available(self): 
        #     print(" ")
        #     # Step 1:  
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     # Step 2: Select the Store View
        #     store_view = "English"   
        #     layered_navigation.select_storeview(store_view)
        #     time.sleep(2) 

        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     layered_navigation.is_category_layered_navigation_heading_there()
        #     assert layered_navigation, "Heading is not displayed." # Use the result for the assertion   
        #     time.sleep(2)

        # @pytest.mark.order(3)
        # def test_expand_all(self): 
        #     print(" ")
        #     print("--")
        #     print("Clicking the expand button.....")
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     # Click on "Expand All"
        #     layered_navigation.click_expand_all() 
        #     print("Successfully Expanded")
            
        # @pytest.mark.order(2)
        # def test_collapse_all(self):
        #     print(" ")
        #     print("--")
        #     # Step 1:  
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     # Step 2: Select the Store View
        #     store_view = "English"   
        #     layered_navigation.select_storeview(store_view)
        #     time.sleep(2) 

        #     print("Clicking the collapse button.....")
        #     layered_navigation = LayeredNavigationPage(self.driver)

        #     # First, expand all categories to ensure we can collapse them
        #     layered_navigation.click_expand_all()
            
        #     # Click on "Collapse All"
        #     layered_navigation.click_collapse_all()
        #     print("Successfully Collapsed")

        # @pytest.mark.order(4)
        # def test_layered_sort_and_filter(self):
        #     # Step 1:  
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     # Step 2: Select the Store View
        #     store_view = "English"   
        #     layered_navigation.select_storeview(store_view)   
        #     layered_navigation.click_expand_all() 
        #     # Locate the first category button in the tree
        #     layered_navigation.select_first_category() 
        #     time.sleep(2)

            
        #     # Step 2: Select the Sort By in Layered Navigation
        #     sort_by_option = "Select only selected attributes in order"
        #     # sort_by_option = "Select all attributes"
        #     layered_navigation.select_sort_option_layered(sort_by_option)
        #     time.sleep(2)
  
        #     # Search in the grid and if its not assigned then assign the attribute to the right side and save
        #     if layered_navigation.search_in_unassign_box("age"):
        #         layered_navigation.enter_15_in_searched_field("Age")  # Enter 15 if the attribute is found
        #         # Step 3: Save the changes
        #         layered_navigation.save_changes()
        #         time.sleep(2)
        #         layered_navigation.select_first_category()
        #     layered_navigation.search_in_assign_box("age") 
        #     layered_navigation.enter_1_in_searched_field("Age")
        #     time.sleep(2)

        # #Check whether the price is correctly assigned to the assigned attributes section (right section)
        # @pytest.mark.order(5)
        # def test_price_in_assigned_list_for_select_all(self):
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     selectAll_sort_by_option = "Select all attributes"
        #     selectOnly_selected_attributes_in_order = "Select only selected attributes in order"

        #     print("-----------")
        #     print("Testing the price has 'X' icon in - 'Select all attributes'")
        #     print("--")
        #     self.driver.refresh()
        #     time.sleep(2)
        #     #Navigate to layered navigations for the category
        #     layered_navigation.click_expand_all() 
        #     # Locate the first category button in the tree
        #     layered_navigation.select_first_category() 
        #     time.sleep(2)
        #     # sort_by_option = "Select all attributes"
        #     layered_navigation.select_sort_option_layered(selectAll_sort_by_option)
        #     time.sleep(2)  
        #     # Verify if 'Price' is in the assigned list
        #     assert layered_navigation.search_in_assign_box("Price"), "'Price' attribute was not assigned to the right side section."
        #     # Verify that the delete button is not available for 'Price'
        #     assert layered_navigation.is_delete_button_visible_for_price(), "Delete button is visible for 'Price' in the assigned list for 'Select all attributes'."

        #     print("--")
        #     print("Testing the price has 'X' icon in - 'Select only selected attributes in order'")
        #     # sort_by_option = "Select only selected attributes in order"
        #     layered_navigation.select_sort_option_layered(selectOnly_selected_attributes_in_order)
        #     time.sleep(2) 

        #     assert layered_navigation.search_in_assign_box("Price"), "'Price' attribute was not assigned to the right side section."
        #     assert layered_navigation.is_delete_button_visible_for_price(), "Delete button is visible for 'Price' in the assigned list for 'Select only selected attributes in order'."

        #Grid view functions tests are as follows
        # @pytest.mark.order(6)
        def test_navigation_gridview(self):
            layered_navigation = LayeredNavigationPage(self.driver) 

            print("-----------")
            print("Testing the Grid View of an category")
            print("--")
            self.driver.refresh()
            time.sleep(2)
            #Navigate to layered navigations for the category
            layered_navigation.click_expand_all() 
            # Locate the first category button in the tree
            layered_navigation.select_first_category() 
            time.sleep(2)

            #locate and go to grid view
            layered_navigation.redirect_gridview()
            time.sleep(2)

        # @pytest.mark.order(7)
        # def test_show_entries_options(self):
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     for value in [12, 24, 36, 66]:
        #         # time.sleep(5)
        #         assert layered_navigation.set_show_entries(value), f"Failed to set and verify show entries to {value}."
        #     layered_navigation.refresh_page()
        #     time.sleep(3)

        # @pytest.mark.order(8)
        # def test_search_functionality(self):
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     layered_navigation.search_in_grid("K-00000240122144715503440")
        #     # value = "K-00000240122144715503440"
        #     # assert layered_navigation.search_in_grid(value), f"Failed to search an product using {value}."
        #     layered_navigation.refresh_page()
        #     time.sleep(3)
        
        # @pytest.mark.order(9)
        # def test_auto_manual_sort(self):
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     manual_count = layered_navigation.count_manual_sorted() 
        #     print(f"Number of manually sorted items: {manual_count}")

        # @pytest.mark.order(10)
        def test_auto_manual_sort(self):
            layered_navigation = LayeredNavigationPage(self.driver)
            has_manual_sorted, manual_sorted_items = layered_navigation.count_manual_sorted()

            # Check if there are at least 3 manually sorted items
            assert has_manual_sorted, "Less than 3 manually sorted items found. Test cannot proceed."

            # Validate sort by sort_number
            sorted_correctly = layered_navigation.check_sort_by_sort_number(manual_sorted_items)
            assert sorted_correctly, "Manually sorted items are not correctly sorted by sort_number."
            print("Test passed: Manually sorted items are correctly sorted by sort_number.")

        # @pytest.mark.order(11)
        def test_auto_manual_sort_update_by_numbering(self):
            layered_navigation = LayeredNavigationPage(self.driver)

            time.sleep(3)
            # Get manually sorted items
            has_manual_sorted, manual_sorted_items = layered_navigation.count_manual_sorted()
            assert has_manual_sorted, "Less than 3 manually sorted items found. Test cannot proceed."

            # Update the sort number for the first manually sorted product
            first_product = manual_sorted_items[0]
            layered_navigation.update_sort_number(first_product, 3)

            # Validate the updated order
            sorted_correctly = layered_navigation.validate_sort_order(manual_sorted_items)
            assert sorted_correctly, "Manually sorted items are not correctly sorted by sort_number after update."

            print("Test passed: Manually sorted items are correctly updated and sorted by sort_number.")
            self.driver.refresh()
            time.sleep(2)

        def test_manual_sort_update_by_dragdrop(self):
            print(" ")
            print("Sorting Manual Products by Drag and Drop.....")
            layered_navigation = LayeredNavigationPage(self.driver)

            time.sleep(3)
            # Get manually sorted items
            has_manual_sorted, manual_sorted_items = layered_navigation.count_manual_sorted()
            assert has_manual_sorted, "Less than 3 manually sorted items found. Test cannot proceed."

            # Update the sort number for the first manually sorted product
            first_product = manual_sorted_items[0]
            layered_navigation.drag_and_drop()

            # Validate the updated order
            sorted_correctly = layered_navigation.validate_sort_order(manual_sorted_items)
            assert sorted_correctly, "Manually sorted items are not correctly sorted by sort_number after update."

            print("Test passed: Manually sorted items are correctly updated and sorted by sort_number.")

        # # @pytest.mark.order(12)
        # def test_disable_enable_of_product(self):
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     layered_navigation.disable_first_product()

        # # @pytest.mark.order(13)
        # def test_disable_enable_of_product(self):
        #     layered_navigation = LayeredNavigationPage(self.driver)
        #     layered_navigation.enable_first_product()
        

    except Exception as e:
            logging.error(f"Error in connection {e}") 