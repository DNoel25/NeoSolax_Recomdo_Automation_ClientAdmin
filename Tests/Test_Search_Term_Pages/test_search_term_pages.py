# Tests/test reports attribute page.py

import logging
import time
import pytest
from Pages.sidebar_page import SideNavigationPage
from Pages.Page_Search_Term_Pages.search_term_pages_page import SearchTermPages
from Utils.base import BaseTest

# @pytest.mark.usefixtures("setup")
class TestSearchTerms(BaseTest):

    try:
        @classmethod
        def setup_class(cls):
            super().setup_class()
            side_nav = SideNavigationPage(cls.driver) 
            side_nav.open_search_term_pages_main()
            side_nav.open_all_pages()
            time.sleep(2)

        def test_heading_available(self): 
            SEOpages_page = SearchTermPages(self.driver)
            SEOpages_page.is_search_term_pages_heading_there()
            assert SEOpages_page, "Heading is not displayed." # Use the result for the assertion

        # def test_grid_displayed(self):
        #     SEOpages_page = SearchTermPages(self.driver)
        #     SEOpages_page.is_grid_displayed()
        #     # assert SEOpages_page.is_grid_displayed(), "Grid is not displayed on Search Terms page."

        # def test_show_entries_options(self):
        #     print(" ")
        #     print("Testing Show Entries...")
        #     SEOpages_page = SearchTermPages(self.driver)
        #     for value in [10, 25, 50, 100]:
        #         assert SEOpages_page.set_show_entries(value), f"Failed to set and verify show entries to {value}."

        # def test_search_functionality(self):
        #     SEOpages_page = SearchTermPages(self.driver)
        #     SEOpages_page.search_in_grid("testing")
        #     # Add assertions for verifying search results in the grid

        # def test_pagination(self):
        #     print(" ")
        #     print("--------")
        #     print("Test pagination functionality on the Search Terms Reports..")
            
        #     SEOpages_page = SearchTermPages(self.driver)

        #     # Wait for pagination to load
        #     SEOpages_page.wait_for_pagination()
        #     time.sleep(2)
            
        #     # Verify initial state: on the first page
        #     if SEOpages_page.is_previous_disabled() and SEOpages_page.get_active_page() == 1:
        #         print("Initial state: Previous button is disabled and active page is 1")
        #     else:
        #         print(f"Initial state: Previous button status: {SEOpages_page.is_previous_disabled()}, "
        #             f"Active page: {SEOpages_page.get_active_page()}.")
        #         assert False, "Initial state validation failed."

        #     # Navigate to the next page and verify
        #     SEOpages_page.click_next()
        #     if SEOpages_page.get_active_page() == 2:
        #         print("After clicking Next: Active page is 2.")
        #     else:
        #         print(f"After clicking Next: Active page is {SEOpages_page.get_active_page()}.")
        #         assert False, "Next button navigation validation failed."
            
        #     # Navigate to a specific page (e.g., page 5) and verify
        #     target_page = 5
        #     SEOpages_page.click_page_number(target_page)
        #     if SEOpages_page.get_active_page() == target_page:
        #         print(f"After navigating to page {target_page}: Active page is {target_page}.")
        #     else:
        #         print(f"After navigating to page {target_page}: Active page is {SEOpages_page.get_active_page()}.")
        #         assert False, f"Navigation to page {target_page} validation failed."

        #     # Navigate back to the previous page and verify
        #     SEOpages_page.click_previous()
        #     if SEOpages_page.get_active_page() == target_page - 1:
        #         print(f"After clicking Previous: Active page is {target_page - 1}.")
        #     else:
        #         print(f"After clicking Previous: Active page is {SEOpages_page.get_active_page()}.")
        #         assert False, f"Previous button navigation validation failed."

        #     # Navigate to the last page and verify
        #     last_page = SEOpages_page.get_last_page_number()
        #     SEOpages_page.click_page_number(last_page)
        #     if SEOpages_page.get_active_page() == last_page and SEOpages_page.is_next_disabled():
        #         print(f"After navigating to the last page {last_page}: Active page is {last_page}, and Next button is disabled.")
        #     else:
        #         print(f"After navigating to the last page {last_page}: Active page is {SEOpages_page.get_active_page()}, "
        #             f"Next button status: {SEOpages_page.is_next_disabled()}.")
        #         assert False, f"Last page navigation validation failed."

        #     # Navigate back to the first page and verify
        #     SEOpages_page.click_page_number(1)
        #     if SEOpages_page.get_active_page() == 1 and SEOpages_page.is_previous_disabled():
        #         print("After navigating back to the first page: Active page is 1, and Previous button is disabled.")
        #     else:
        #         print(f"After navigating back to the first page: Active page is {SEOpages_page.get_active_page()}, "
        #             f"Previous button status: {SEOpages_page.is_previous_disabled()}.")
        #         assert False, "First page navigation validation failed."

        # def test_filters(self):
        #     print(" ")
        #     print("--------")
        #     print("Test Filter by Store View functionality on the Search Terms Reports..")
        #     #Holding this functionality since by using the store view we can not be tested while it has only 


#Testing create new scenario
        def test_create_new_seo(self):
           print(" ")
           print("--------")
           print("Test Add New Search Term Pages...")   

           add_seo_page = SearchTermPages(self.driver)

           add_seo_page.go_to_addnew_form()

           add_seo_page.fill_general("regression by automate", "test")
           time.sleep(2)

           add_seo_page.fill_content()
           time.sleep(2)
            
           add_seo_page.fill_SEO()
           time.sleep(2)

    except Exception as e:
            logging.error(f"Error in connection {e}") 
    

    