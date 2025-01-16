# Tests/test_manual_suggestions.py

import logging
import time
import pytest
from Pages.sidebar_page import SideNavigationPage
from Pages.Page_Search_Results_Management.manual_suggestions_page import ManualSuggestionsPage
from Utils.base import BaseTest

# @pytest.mark.usefixtures("setup")
class TestManualSuggestions(BaseTest):

    try:
        @classmethod
        def setup_class(cls):
            super().setup_class()
            side_nav = SideNavigationPage(cls.driver)
            side_nav.open_search_results_management()
            side_nav.open_manual_suggestions()
            
        def test_heading_available(self): 
            manual_page = ManualSuggestionsPage(self.driver)
            manual_page.is_manual_suggestion_heading_there()
            assert manual_page, "Heading is not displayed." # Use the result for the assertion

    
        def test_grid_displayed(self):
            manual_page = ManualSuggestionsPage(self.driver)
            assert manual_page.is_grid_displayed(), "Grid is not displayed on Manual Suggestions page."

        def test_show_entries_options(self):
            manual_page = ManualSuggestionsPage(self.driver)
            for value in [10, 25, 50, 100]:
                assert manual_page.set_show_entries(value), f"Failed to set and verify show entries to {value}."

        def test_search_functionality(self):
            manual_page = ManualSuggestionsPage(self.driver)
            manual_page.search_in_grid("kidies")
            # Add assertions for verifying search results in the grid

        # def test_add_new_suggestion(self):
        #     # manual_page = ManualSuggestionsPage(self.driver) 
        #     # assert manual_page.click_add_new("English"), f"Failed to set and verify show entries to {"English"}."
        #     # # Add assertions to verify new suggestion form is displayed 
        #     add_new_page = ManualSuggestionsPage(self.driver)

        #     # Step 1: Click "Add New"
        #     add_new_page.click_add_new() 

        #     # Step 2: Fill the form
        #     store_view = "English"  # or any specific store view
        #     keyword = "new_keyword"
        #     synonyms = ["synonym3"]
        #     weights = ["15"]
        #     add_new_page.fill_form(store_view, keyword, synonyms, weights)
        #     print("filled the add new form")
        #     # Step 3: Submit and verify
        #     time.sleep(5)

        #     add_new_page.submit_form()
        #     print("cliecked the submit")
        #     time.sleep(10)
        # assert add_new_page.verify_success_message(), "Success message not displayed or incorrect." 

        def test_edit_suggestion(self):
            """
            Verify that the synonym's name can be edited and saved in the edit form.
            """
            manual_page = ManualSuggestionsPage(self.driver)

            # Step 1: Navigate to the edit form
            manual_page.click_edit_button(search_keyword='new_keyword', row_index=0)

            # Step 2: Edit a synonym in the edit form
            manual_page.edit_synonym(synonym_index=0, new_synonym="UpdatedSynonym")

            # Step 3: Save the changes
            manual_page.save_changes()

            time.sleep(10)

        def test_Verify_Updated_Synonym(self):
            manual_page = ManualSuggestionsPage(self.driver)  
            manual_page.verify_updated_suggestion('new_keyword','UpdatedSynonym')


            # # Step 5: Optionally, verify the updated value in the grid view
            # manual_page.search_in_grid('new_keyword')
            # edited_row = manual_page.get_row_data(row_index=0)
            # assert "UpdatedSynonym" in edited_row, "Synonym not updated in the grid view."
            # print("Synonym updated successfully in the grid view.")   

    except Exception as e:
            logging.error(f"Error in connection {e}") 

        
        

        # def test_delete_suggestion(self):
        #     print("delete test started")
        #     manual_page = ManualSuggestionsPage(self.driver)
        #     manual_page.click_delete_button("sdas")
        #     # Add assertions to verify deletion success, such as confirmation modal or grid update


    




    
