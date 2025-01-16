# Tests/test reports attribute page.py

import logging
import time
import pytest
from Pages.sidebar_page import SideNavigationPage
from Pages.Page_Reports_Management.ai_suggestion_page import AI_Suggestion
from Utils.base import BaseTest

# @pytest.mark.usefixtures("setup")
class TestSearchTerms(BaseTest):

    try:
        @classmethod
        def setup_class(cls):
            super().setup_class()
            side_nav = SideNavigationPage(cls.driver) 
            side_nav.open_report_management()
            side_nav.open_ai_suggestions_page()
            time.sleep(2)

        def test_heading_available(self): 
            ai_suggestion_page = AI_Suggestion(self.driver)
            ai_suggestion_page.is_ai_suggestions_page_heading_there()
            assert ai_suggestion_page, "Heading is not displayed." # Use the result for the assertion

        def test_grid_displayed(self):
            ai_suggestion_page = AI_Suggestion(self.driver)
            ai_suggestion_page.is_grid_displayed()
            # assert ai_suggestion_page.is_grid_displayed(), "Grid is not displayed on Search Terms page."

        def test_show_entries_options(self):
            print(" ")
            print("Testing Show Entries...")
            ai_suggestion_page = AI_Suggestion(self.driver)
            for value in [10, 25, 50, 100]:
                assert ai_suggestion_page.set_show_entries(value), f"Failed to set and verify show entries to {value}."

        def test_search_functionality(self):
            ai_suggestion_page = AI_Suggestion(self.driver)
            ai_suggestion_page.search_in_grid("health-safety-ecoclean")
            # Add assertions for verifying search results in the grid

        def test_pagination(self):
            print(" ")
            print("--------")
            print("Test pagination functionality on the Search Terms Reports..")
            
            ai_suggestion_page = AI_Suggestion(self.driver)

            # Wait for pagination to load
            ai_suggestion_page.wait_for_pagination()

            # Verify initial state: on the first page
            if ai_suggestion_page.is_previous_disabled() and ai_suggestion_page.get_active_page() == 1:
                print("Initial state: Previous button is disabled and active page is 1")
            else:
                print(f"Initial state: Previous button status: {ai_suggestion_page.is_previous_disabled()}, "
                    f"Active page: {ai_suggestion_page.get_active_page()}.")
                assert False, "Initial state validation failed."

            # Navigate to the next page and verify
            ai_suggestion_page.click_next()
            if ai_suggestion_page.get_active_page() == 2:
                print("After clicking Next: Active page is 2.")
            else:
                print(f"After clicking Next: Active page is {ai_suggestion_page.get_active_page()}.")
                assert False, "Next button navigation validation failed."
            
            # Navigate to a specific page (e.g., page 5) and verify
            target_page = 5
            ai_suggestion_page.click_page_number(target_page)
            if ai_suggestion_page.get_active_page() == target_page:
                print(f"After navigating to page {target_page}: Active page is {target_page}.")
            else:
                print(f"After navigating to page {target_page}: Active page is {ai_suggestion_page.get_active_page()}.")
                assert False, f"Navigation to page {target_page} validation failed."

            # Navigate back to the previous page and verify
            ai_suggestion_page.click_previous()
            if ai_suggestion_page.get_active_page() == target_page - 1:
                print(f"After clicking Previous: Active page is {target_page - 1}.")
            else:
                print(f"After clicking Previous: Active page is {ai_suggestion_page.get_active_page()}.")
                assert False, f"Previous button navigation validation failed."

            # # Navigate to the last page and verify
            # last_page = ai_suggestion_page.get_last_page_number()
            # ai_suggestion_page.click_page_number(last_page)
            # if ai_suggestion_page.get_active_page() == last_page and ai_suggestion_page.is_next_disabled():
            #     print(f"After navigating to the last page {last_page}: Active page is {last_page}, and Next button is disabled.")
            # else:
            #     print(f"After navigating to the last page {last_page}: Active page is {ai_suggestion_page.get_active_page()}, "
            #         f"Next button status: {ai_suggestion_page.is_next_disabled()}.")
            #     assert False, f"Last page navigation validation failed."

            # Navigate back to the first page and verify
            ai_suggestion_page.click_page_number(1)
            if ai_suggestion_page.get_active_page() == 1 and ai_suggestion_page.is_previous_disabled():
                print("After navigating back to the first page: Active page is 1, and Previous button is disabled.")
            else:
                print(f"After navigating back to the first page: Active page is {ai_suggestion_page.get_active_page()}, "
                    f"Previous button status: {ai_suggestion_page.is_previous_disabled()}.")
                assert False, "First page navigation validation failed."

        # def test_filters(self):
        #     print(" ")
        #     print("--------")
        #     print("Test Filter by Store View functionality on the Search Terms Reports..")
        #     #Holding this functionality since by using the store view we can not be tested while it has only 

    except Exception as e:
            logging.error(f"Error in connection {e}") 
    

    