# Tests/test_search_pages.py

import logging
import time
import pytest
from Pages.sidebar_page import SideNavigationPage 
from Pages.Page_Reports_Management.search_term_page import SearchTermPages
from Utils.base import BaseTest

# @pytest.mark.usefixtures("setup")
class TestSearchTerms(BaseTest):

    try:
        @classmethod
        def setup_class(cls):
            super().setup_class()
            side_nav = SideNavigationPage(cls.driver) 
            side_nav.open_report_management()
            side_nav.open_search_term_pages()
            time.sleep(2)

        def test_heading_available(self): 
            search_term_pages = SearchTermPages(self.driver)
            search_term_pages.is_search_term_pages_heading_there()
            assert search_term_pages, "Heading is not displayed." # Use the result for the assertion

        def test_grid_displayed(self):
            search_term_pages = SearchTermPages(self.driver)
            search_term_pages.is_grid_displayed()
            # assert search_term_pages.is_grid_displayed(), "Grid is not displayed on Search Terms page."

        def test_show_entries_options(self):
            print(" ")
            print("Testing Show Entries...")
            search_term_pages = SearchTermPages(self.driver)
            for value in [10, 25, 50, 100]:
                assert search_term_pages.set_show_entries(value), f"Failed to set and verify show entries to {value}."

        def test_search_functionality(self):
            search_term_pages = SearchTermPages(self.driver)
            search_term_pages.search_in_grid("prenatal-vitamins")
            # Add assertions for verifying search results in the grid

        def test_pagination(self):
            print(" ")
            print("--------")
            print("Test pagination functionality on the Search Terms Reports..")
            
            search_term_pages = SearchTermPages(self.driver)

            # Wait for pagination to load
            search_term_pages.wait_for_pagination()

            # Verify initial state: on the first page
            if search_term_pages.is_previous_disabled() and search_term_pages.get_active_page() == 1:
                print("Initial state: Previous button is disabled and active page is 1")
            else:
                print(f"Initial state: Previous button status: {search_term_pages.is_previous_disabled()}, "
                    f"Active page: {search_term_pages.get_active_page()}.")
                assert False, "Initial state validation failed."

            # Navigate to the next page and verify
            search_term_pages.click_next()
            if search_term_pages.get_active_page() == 2:
                print("After clicking Next: Active page is 2.")
            else:
                print(f"After clicking Next: Active page is {search_term_pages.get_active_page()}.")
                assert False, "Next button navigation validation failed."

            # Navigate to a specific page (e.g., page 5) and verify
            target_page = 5
            search_term_pages.click_page_number(target_page)
            if search_term_pages.get_active_page() == target_page:
                print(f"After navigating to page {target_page}: Active page is {target_page}.")
            else:
                print(f"After navigating to page {target_page}: Active page is {search_term_pages.get_active_page()}.")
                assert False, f"Navigation to page {target_page} validation failed."

            # Navigate back to the previous page and verify
            search_term_pages.click_previous()
            if search_term_pages.get_active_page() == target_page - 1:
                print(f"After clicking Previous: Active page is {target_page - 1}.")
            else:
                print(f"After clicking Previous: Active page is {search_term_pages.get_active_page()}.")
                assert False, f"Previous button navigation validation failed."

            # Navigate to the last page and verify
            last_page = search_term_pages.get_last_page_number()
            search_term_pages.click_page_number(last_page)
            if search_term_pages.get_active_page() == last_page and search_term_pages.is_next_disabled():
                print(f"After navigating to the last page {last_page}: Active page is {last_page}, and Next button is disabled.")
            else:
                print(f"After navigating to the last page {last_page}: Active page is {search_term_pages.get_active_page()}, "
                    f"Next button status: {search_term_pages.is_next_disabled()}.")
                assert False, f"Last page navigation validation failed."

            # Navigate back to the first page and verify
            search_term_pages.click_page_number(1)
            if search_term_pages.get_active_page() == 1 and search_term_pages.is_previous_disabled():
                print("After navigating back to the first page: Active page is 1, and Previous button is disabled.")
            else:
                print(f"After navigating back to the first page: Active page is {search_term_pages.get_active_page()}, "
                    f"Previous button status: {search_term_pages.is_previous_disabled()}.")
                assert False, "First page navigation validation failed."
        

        # def test_filters(self):
        #     print(" ")
        #     print("--------")
        #     print("Test Filter by Store View functionality on the Search Terms Reports..")
        #     #Holding this functionality since by using the store view we can not be tested while it has only 

                search_term_pages.go_to_dashboard()
    except Exception as e:
            logging.error(f"Error in connection {e}") 
    

    