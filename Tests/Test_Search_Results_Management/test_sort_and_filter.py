from Pages.sidebar_page import SideNavigationPage
from Pages.Page_Search_Results_Management.search_sort_and_filter_page import SearchSortAndFilter
from Utils.base import BaseTest
import time
import pytest
# @pytest.mark.usefixtures("setup")
class TestSortAndFilter(BaseTest):
    try:
        @classmethod
        def setup_class(cls):
            super().setup_class()
            side_nav1 = SideNavigationPage(cls.driver)
            side_nav1.open_search_results_management()
            side_nav1.open_sort_and_filter()

        def test_heading_available(self): 
            search_sort_page = SearchSortAndFilter(self.driver)
            search_sort_page.is_advanced_sortandfilter_heading_there()
            assert search_sort_page, "Heading is not displayed." # Use the result for the assertion   
        
        def test_layered_sort_and_filter(self):
            # Step 1: 
            advanced_sort_and_filter = SearchSortAndFilter(self.driver)
            # Step 2: Select the Store View
            store_view = "English"   
            advanced_sort_and_filter.select_storeview(store_view)
            time.sleep(2) 

            # Step 2: Select the Sort By in Layered Navigation
            sort_by_option = "Select only selected attributes in order"
            # sort_by_option = "Select all attributes"
            advanced_sort_and_filter.select_sort_option_layered(sort_by_option)
            time.sleep(2)
  
            # Search in the grid and if its not assigned then assign the attribute to the right side and save
            if advanced_sort_and_filter.search_in_assign_box("age"):
                advanced_sort_and_filter.enter_15_in_searched_field("Age")  # Enter 15 if the attribute is found
                # Step 3: Save the changes
                advanced_sort_and_filter.save_changes()
                time.sleep(2)
            advanced_sort_and_filter.search_in_assign_box("age") 
            advanced_sort_and_filter.enter_1_in_searched_field("Age")

        #Check whether the price is correctly assigned to the assigned attributes section (right section)
        def test_price_in_assigned_list_for_select_all(self):
            advanced_sort_and_filter1 = SearchSortAndFilter(self.driver)
            selectAll_sort_by_option = "Select all attributes"
            selectOnly_selected_attributes_in_order = "Select only selected attributes in order"
            
            print("-----------")
            print("Testing the price has 'X' icon in - 'Select all attributes'")
            print("--")
            self.driver.refresh()
            time.sleep(2)
            # sort_by_option = "Select all attributes"
            advanced_sort_and_filter1.select_sort_option_layered1(selectAll_sort_by_option)
            time.sleep(2)  
            # Verify if 'Price' is in the assigned list
            assert advanced_sort_and_filter1.search_in_assign_box("Price"), "'Price' attribute was not assigned to the right side section."
            # Verify that the delete button is not available for 'Price'
            assert advanced_sort_and_filter1.is_delete_button_visible_for_price(), "Delete button is visible for 'Price' in the assigned list for 'Select all attributes'."

            print("--")
            print("Testing the price has 'X' icon in - 'Select only selected attributes in order'")
            # sort_by_option = "Select only selected attributes in order"
            advanced_sort_and_filter1.select_sort_option_layered(selectOnly_selected_attributes_in_order)
            time.sleep(2) 

            assert advanced_sort_and_filter1.search_in_assign_box("Price"), "'Price' attribute was not assigned to the right side section."
            assert advanced_sort_and_filter1.is_delete_button_visible_for_price(), "Delete button is visible for 'Price' in the assigned list for 'Select only selected attributes in order'."

        #STARTING THE TEST on SORT BY OPTION FILTER
        def test_sort_by(self):
            print("-------")
            print("Starting the testing for SORT BY OPTION FILTERS")
            # Step 1: 
            advanced_sort_and_filter = SearchSortAndFilter(self.driver)
            # Step 2: Select the Store View
            store_view = "English"   
            advanced_sort_and_filter.select_storeview(store_view)
            time.sleep(2) 

            # Step 2: Select the Sort By in Layered Navigation
            sort_by_option = "Select only selected attributes in order"
            # sort_by_option = "Select all attributes"
            advanced_sort_and_filter.select_sort_option_sortby(sort_by_option)
            time.sleep(2)
  
            # Search in the grid and if its not assigned then assign the attribute to the right side and save
            if advanced_sort_and_filter.search_in_sortby_assign_box("Product Name"):
                advanced_sort_and_filter.enter_15_in_sortby_searched_field("Product Name")  # Enter 15 if the attribute is found
                # Step 3: Save the changes
                advanced_sort_and_filter.save_changes()
                time.sleep(2)
            # advanced_sort_and_filter.search_in_sortby_assign_box("product name") 
            # advanced_sort_and_filter.enter_1_in_sortby_searched_field("product name")

    except Exception as e:
            logging.error(f"Error in connection {e}") 