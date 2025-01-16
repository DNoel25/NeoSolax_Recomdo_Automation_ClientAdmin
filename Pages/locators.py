# Pages/locators.py

from selenium.webdriver.common.by import By

class Locators:

#Dashboard module
    DASHBOARD_MODULE_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-tachometer-alt")])[1]'))
#Search Results Management Module
    SEARCH_RESULTS_MANAGEMENT_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
    MANUAL_SUGGESTION_SUBMODULE = ((By.XPATH, '//a[contains(text(), "Manual Suggestions")]'))
    # SEARCH_SORT_AND_FILTER = (By.XPATH, '//a[contains(text(), "Advanced Sort & Filter")]')
    SEARCH_SORT_AND_FILTER = (By.XPATH, '/html/body/div/aside/div/nav/ul/li[4]/ul/li[2]/a')


    # SEARCH_SORT_AND_FILTER = ((By.XPATH, '//a[contains(text(), "Advanced Sort & Filter")]'))
    
    #--- Manual Suggestions Page locators ---#
    Heading = (By.TAG_NAME, "h2")
    GRID_VIEW = (By.ID, "SuggestionTable_wrapper")  # Grid view element ID
    SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='SuggestionTable_length' and @aria-controls='SuggestionTable']"))  # Dropdown for entries shown per page
    SEARCH_FIELD = (By.ID, "search")  # Search filter field
    GRID_ACTIONS_COLUMN = (By.CSS_SELECTOR, ".grid-actions")  # Actions column in the grid 
    EDIT_BUTTON = (By.XPATH, "(//a[@title='Edit'])[1]")  # Edit button selector for the first row in the grid
    DELETE_BUTTON = (By.CSS_SELECTOR, ".delete-action")  # Delete button selector in grid
    STORE_VIEW_DROPDOWN = ((By.XPATH, "//select")) 
    # Add New Form Locators
     # Locators for form fields
    ADD_NEW_BUTTON = (By.ID, "add_suggestion")  # Add new manual suggestion button
    STORE_VIEW_DROPDOWN = (By.XPATH, "//select[@name='store_view' and @id='store_view_select']")  # Update with actual name
    KEYWORD_FIELD = (By.NAME, "old_search_keyword")  # Update with actual name
    SYNONYM_FIELD = (By.XPATH, "//input[@class='synonyms_field synonyms_field_default bg-white-50 border border-gray-300 rounded-lg']")  # Update if different
    WEIGHT_FIELD = (By.XPATH, "//input[@id='weight_field_id']")  # Update if different
    SAVE_BUTTON = (By.XPATH, "//button[@id='save_suggestion_data']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    #SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success') and contains(text(), 'Data Added successfully!')]")


    #Locators for Advanced Sort & Filter
    ASF_STORE_VIEW_DROPDOWN = (By.XPATH, "//select[@name='store_view_select' and @id='store_view_select']")
    ASF_SORTOPTION_LAYERED = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[2]/div[2]/section/div/div[1]/div[2]/select")
    ASF_SAVE_BUTTON = (By.XPATH, "//button[@id='save_attribute_sort']")
    ASF_SEARCH_TEXT = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[2]/div[2]/section/div/div[2]/div[2]/div/div[1]/div[1]/input")
    ASF_UNASSIGNED_LIST = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[2]/div[2]/section/div/div[2]/div[2]/div/div[1]/div[2]/ul")
    #Locators for Sort By Options
    ASF_SORTOPTION_SORTBY = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[3]/div[2]/section/div/div[1]/div[2]/select")
    
#Category Management
    CATEGORY_MANAGEMENT_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-tasks")])[1]'))
    LAYERED_NAVIGATION_SUBMODULE = ((By.XPATH, '//a[contains(text(), "Layered Navigation Sorting")]'))

    EXPAND_ALL = ((By.XPATH, '//*[@id="expand_all"]'))
    COLLAPSE_ALL = ((By.XPATH, '//*[@id="collapse_all"]'))
    CM_STORE_VIEW_DROPDOWN = (By.XPATH, "//select[@name='store_view_select' and @id='store_view_select']")
    CM_SORTOPTION_LAYERED = (By.XPATH, "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[2]/div/div/div[2]/div[3]/div[1]/div[2]/select")
    CM_SAVE_BUTTON = (By.XPATH, "//button[@id='save_category_attribute_sort']")
    CM_SEARCH_TEXT = (By.XPATH, "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/input")
    CM_UNASSIGNED_LIST = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[2]/div[2]/section/div/div[2]/div[2]/div/div[1]/div[2]/ul")
    
    #Locators for Sort By Options
    ASF_SORTOPTION_SORTBY = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[3]/div[2]/section/div/div[1]/div[2]/select")

    #Locators for Grid view
    CM_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@id='products-per-page']"))  # Dropdown for entries shown per page
    # CM_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='SuggestionTable_length' and @aria-controls='SuggestionTable']"))  # Dropdown for entries shown per page 
    CM_SAVE_BUTTON_IN_CATEGORY_GRID = (By.XPATH, "//button[@id='save_product_sort']")


#Report Management 
    RM_REPORT_MANAGEMENT_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-book")])[1]')) 
    #-----
    RM_SEARCH_TERMS_SUBMODULE = (By.XPATH, '//a[@href="/client-admin/report/search-terms/"]')
    
    RMST_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='searchTermsTable_length' and @aria-controls='searchTermsTable']"))  # Dropdown for entries shown per page
    RMST_SEARCH_FIELD = (By.ID, "searchTermsTable_filter")  # Search filter field
    RMST_PAGINATION_CONTAINER = (By.ID, "searchTermsTable_paginate")
    RMST_PREVIOUS_BUTTON = (By.ID, "searchTermsTable_previous")
    RMST_NEXT_BUTTON = (By.ID, "searchTermsTable_next")
    RMST_PAGE_NUMBERS = (By.CSS_SELECTOR, ".paginate_button:not(.next):not(.previous)")
    RMST_LAST_PAGE_NUMBER = (By.XPATH,
        '//a[contains(@class, "paginate_button") and not(contains(@aria-controls, "previous")) and not(contains(@aria-controls, "next"))][last()]')
    RMST_FILTER_BUTTON = (By.ID, "filter_section_view") 

    #-----
    RMST_SEARCH_TERM_PAGES_SUBMODULE = (By.XPATH, '//a[@href="/client-admin/report/seo-pages/"]')

    RMSTP_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='seoSearchCountTable_length' and @aria-controls='seoSearchCountTable']"))  # Dropdown for entries shown per page
    # RMSTP_SEARCH_FIELD = (By.type, "search")  # Search filter field
    RMSTP_PAGINATION_CONTAINER = (By.ID, "seoSearchCountTable_paginate")
    RMSTP_PREVIOUS_BUTTON = (By.ID, "seoSearchCountTable_previous")
    RMSTP_NEXT_BUTTON = (By.ID, "seoSearchCountTable_next")
    RMSTP_PAGE_NUMBERS = (By.CSS_SELECTOR, ".paginate_button:not(.next):not(.previous)")
    RMSTP_LAST_PAGE_NUMBER = (By.XPATH,
        '//a[contains(@class, "paginate_button") and not(contains(@aria-controls, "previous")) and not(contains(@aria-controls, "next"))][last()]')
    RMSTP_FILTER_BUTTON = (By.ID, "filter_section_view")


    #-----
    RMAP_ATTRIBUTE_PAGE_SUBMODULE = (By.XPATH, '//a[@href="/client-admin/report/attribute-pages/"]')

    RMAP_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='attributeSearchCountTable_length' and @aria-controls='attributeSearchCountTable']"))  # Dropdown for entries shown per page
    # RMSTP_SEARCH_FIELD = (By.type, "search")  # Search filter field
    RMAP_PAGINATION_CONTAINER = (By.ID, "attributeSearchCountTable_paginate")
    RMAP_PREVIOUS_BUTTON = (By.ID, "attributeSearchCountTable_previous")
    RMAP_NEXT_BUTTON = (By.ID, "attributeSearchCountTable_next")
    RMAP_PAGE_NUMBERS = (By.CSS_SELECTOR, ".paginate_button:not(.next):not(.previous)")
    RMAP_LAST_PAGE_NUMBER = (By.XPATH,  
        '//a[contains(@class, "paginate_button") and not(contains(@aria-controls, "previous")) and not(contains(@aria-controls, "next"))][last()]')
    RMAP_FILTER_BUTTON = (By.ID, "filter_section_view")


    #-----
    RMAI_AI_SUGGESTIONS_SUBMODULE = (By.XPATH, '//a[@href="/client-admin/report/suggestions/"]')

    RMAI_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='suggestionsResultsTable_length' and @aria-controls='suggestionsResultsTable']"))  # Dropdown for entries shown per page
    # RMSTP_SEARCH_FIELD = (By.type, "search")  # Search filter field
    RMAI_PAGINATION_CONTAINER = (By.ID, "suggestionsResultsTable_paginate")
    RMAI_PREVIOUS_BUTTON = (By.ID, "suggestionsResultsTable_previous")
    RMAI_NEXT_BUTTON = (By.ID, "suggestionsResultsTable_next")
    RMAI_PAGE_NUMBERS = (By.CSS_SELECTOR, ".paginate_button:not(.next):not(.previous)")
    RMAI_LAST_PAGE_NUMBER = (By.XPATH,  
        '//a[contains(@class, "paginate_button") and not(contains(@aria-controls, "previous")) and not(contains(@aria-controls, "next"))][last()]')
    RMAI_FILTER_BUTTON = (By.ID, "filter_section_view")

#Search Term Pages 
    ST_SEARCH_TERM_PAGES_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fa-solid fa-sitemap")])[1]')) 
    #-----
    STAP_ALL_PAGES_SUBMODULE = (By.XPATH, '//a[@href="/client-admin/seo/index/"]')
    
    STAP_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='allPageTable_length' and @aria-controls='allPageTable']"))  # Dropdown for entries shown per page
    STAP_SEARCH_FIELD = (By.ID, "allPageTable_filter")  # Search filter field
    STAP_PAGINATION_CONTAINER = (By.ID, "allPageTable_paginate")
    STAP_PREVIOUS_BUTTON = (By.ID, "allPageTable_previous")
    STAP_NEXT_BUTTON = (By.ID, "allPageTable_next")
    STAP_PAGE_NUMBERS = (By.CSS_SELECTOR, ".paginate_button:not(.next):not(.previous)")
    STAP_LAST_PAGE_NUMBER = (By.XPATH,
        '//a[contains(@class, "paginate_button") and not(contains(@aria-controls, "previous")) and not(contains(@aria-controls, "next"))][last()]')
    STAP_FILTER_BUTTON = (By.ID, "filter_section_view") 

    #-----
    #Adding new search term pages
    ST_CREATE_NEW_BUTTON = (By.CSS_SELECTOR, "a.back-button.view")
    STCN_ENABLE_SEO_CHECKBOX = (By.ID, "is_active")
    STCN_TITLE_INPUT = (By.ID, "category_name")
    STCN_KEYWORD_INPUT = (By.ID, "search_keyword")
    STCN_STORE_VIEW_DROPDOWN = (By.ID, "store_view")