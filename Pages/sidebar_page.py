# Pages/side_navigation_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators

class SideNavigationPage:
    def __init__(self, driver):
        self.driver = driver

#Dashboard module 
    def open_dashboard_menu(self):
        # Wait for and click on the "Search Results Management" main menu item by indexing
        dashboard_module = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.DASHBOARD_MODULE_MENU)
        )
        dashboard_module.click() 

#Search Results Management Module
    def open_search_results_management(self):
        # Wait for and click on the "Search Results Management" main menu item by indexing
        search_results_management = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.SEARCH_RESULTS_MANAGEMENT_MENU)
        )
        search_results_management.click()
        print("Main menu item 'Search Results Management' clicked")

    def open_manual_suggestions(self):
        # Wait for and click on the "Manual Suggestions" submodule item by unique text or order
        manual_suggestions = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Manual Suggestions")]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.MANUAL_SUGGESTION_SUBMODULE)
        )
        manual_suggestions.click()
        print("Submodule 'Manual Suggestions' clicked")
    
    def open_sort_and_filter(self): 
        # Wait for and click on the "Manual Suggestions" submodule item by unique text or order
        avanced_sort_and_filter = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Manual Suggestions")]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.SEARCH_SORT_AND_FILTER)
        ) 
        avanced_sort_and_filter.click()
        print("Submodule 'Advanced Sort & Filter' clicked")

#Category Management Module

    def open_category_management(self):
        # Wait for and click on the "Search Results Management" main menu item by indexing
        category_management = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.CATEGORY_MANAGEMENT_MENU)
        )
        category_management.click()
        print("Main menu item 'Category Management' clicked")

    def open_layered_navigation(self):
        # Wait for and click on the "Manual Suggestions" submodule item by unique text or order
        layered_navigation = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Manual Suggestions")]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.LAYERED_NAVIGATION_SUBMODULE)
        )
        layered_navigation.click()
        print("Submodule 'layered_navigation' clicked")

#Report Management

    def open_report_management(self):
        report_management = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.RM_REPORT_MANAGEMENT_MENU)
        )
        report_management.click()
        print("Main Module 'Report Management' clicked ")
    
    def open_search_terms(self):
        search_terms = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.RM_SEARCH_TERMS_SUBMODULE)
        )
        search_terms.click()
        print("Submodule 'Search Terms' clicked")

    def open_search_term_pages(self):
        search_terms = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.RMST_SEARCH_TERM_PAGES_SUBMODULE)
        )
        search_terms.click()
        print("Submodule 'Search Terms' clicked")
    
    def open_attribute_page(self):
        search_terms = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.RMAP_ATTRIBUTE_PAGE_SUBMODULE)
        )
        search_terms.click()
        print("Submodule 'Search Terms' clicked")

    def open_ai_suggestions_page(self):
        search_terms = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.RMAI_AI_SUGGESTIONS_SUBMODULE)
        )
        search_terms.click()
        print("Submodule 'Search Terms' clicked")

#Search Term Pages
    def open_search_term_pages_main(self):
        report_management = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ST_SEARCH_TERM_PAGES_MENU)
        )
        report_management.click()
        print("Main Module 'Search Term Pages' clicked ")
    
    def open_all_pages(self):
        search_terms = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.STAP_ALL_PAGES_SUBMODULE)
        )
        search_terms.click()
        print("Submodule 'All Pages' clicked")