import sys

import moodle_locators as locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # <---add this import for drop down list
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code
# s = Service(executable_path='C:\\Users\\aamykutty\\PycharmProjects\\pythonProject\\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
#-----------------GIthub------
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# ------------------------------------------------------------
# driver=webdriver.Chrome('chromedriver.exe')
# driver = webdriver.Chrome('C:\\Users\\aamykutty\\PycharmProjects\\pythonProject\\chromedriver.exe')

def setup():
    print("Lanunch Moodle App")
    print("--------------------------------")
    # browser full screen
    driver.maximize_window()

    # Give browser 30 sec to respond
    driver.implicitly_wait(5)

    # Navigate to moodle app website
    driver.get(f'{locators.moodle_url}')

    # Check that Moodle url and the home page title are displayed
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print(f'Yey!!! {locators.app}Launched successfully')
        print(f'{locators.app} Home page URL= {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(5)

    else:
        print(f'{locators.app} is not Launched!!! Check your code or application')
        print(f'{locators.app} Home page URL: {driver.current_url}\nHome Page Title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print('---------------------------------------')
        print(f'The is completed at:{datetime.datetime.now()} ')
        sleep(2)
        driver.close()
        driver.quit()


def log_in(username, password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()

        if driver.current_url == locators.moodle_login_page_url:

            print(f'{locators.app} App Login Page is Displayed')
            sleep(1)
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(1)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(1)
            driver.find_element(By.ID, 'loginbtn').click()  # Method 1 using ID
            # --------------------------------------------------------------------------------------------------------------------------------------
            # XPATH

            # driver.find_element(By.XPATH,'//button[contains(.,"Log in")]').click()         #Method 2 xpath using any thing with text 'Log in'
            # driver.find_element(By.XPATH,'//button[contains(@id,"loginbtn")]').click()     #Method 3: XPATH using specific id
            # driver.find_element(By.XPATH,'//button[@id="loginbtn"]').click()               #Method 4: XPATH without conatins
            # driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()                   #Method 5: XPATH without tag name

            # ---------------------------------------------------------------------------------------------------------------------

            # CSS Selector
            # driver.find_element(By.CSS_SELECTOR,'button[id= "loginbtn"]').click()            #Method 1: CSS SELECTOR
            # driver.find_element(By.CSS_SELECTOR, 'button#loginbtn').click()                  #Method 2: CSS SELECTOR

            # -------------------------------------------------------------------------------------------------------------------------------------------

            # Validate we are at the dashboard
            if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                assert driver.title == locators.moodle_dashboard_page_title
                print(
                    f'---- Login Successful !!{locators.app} Dashboard is displayed ------\nPage Title: {driver.title}')
                sleep(5)
            else:
                print(f'xxxx----Dashboard is not displayed.Check your code and try again----xxxxxxxx')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    if driver.current_url == locators.moodle_url:
        print(f'---- Log out Succussful: {datetime.datetime.now()}----')
        sleep(5)


def create_new_user():
    # navigate to the site administration
    sleep(5)
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(1)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(1)
    # validate we are in 'Add a new user page'
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.moodle_add_new_user_page_title
    print(f'Navigate to Add New User Page : {driver.title}')
    # breakpoint()
    sleep(1)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(1)

    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(.25)
    # select an oprtion "Allow everyone to see my email address"
    sleep(1)
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text(
        'Allow everyone to see my email address')
    sleep(.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(1)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(1)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(1)
    # upload a picture
    # click arrow element
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(1)
    # navigate to imga selection
    # driver.find_element(By.LINK_TEXT,'Server files').click()
    # sleep(1)
    # driver.find_element(By.LINK_TEXT,'sl_Frozen').click()
    # sleep(1)
    # driver.find_element(By.LINK_TEXT,'sl_How to build a snowman').click()
    # sleep(1)
    # driver.find_element(By.LINK_TEXT,'Course image').click()
    # sleep(1)
    # driver.find_element(By.LINK_TEXT,'gieEd4R5T.png').click()
    # sleep(1)

    img_path = ['Server files', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in img_path:
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(1)
    # select a radio button
    # driver.find_element(By.XPATH,'//input[@value="4"]').click()  #method 1
    driver.find_element(By.XPATH, '//label[contains(.,"Create an alias/shortcut to the file")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(1)
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    sleep(.25)
    # populate Additional Name
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    sleep(.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    sleep(.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    sleep(.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)
    sleep(.25)
    driver.find_element(By.LINK_TEXT, 'Interests').click()
    sleep(.25)
    for tag in locators.list_of_interests:
        # sleep(1)
        # driver.find_element(By.XPATH,'//input[contains(@id, "form_autocomplete_input")]').send_keys(tag)
        # sleep(1)
        # driver.find_element(By.XPATH,'//input[contains(@id, "form_autocomplete_input")]').send_keys(Keys.ENTER)
        # sleep(1)

        # Method 2
        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag + Keys.ENTER)

        # Method3
        # driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag + "\n")

    driver.find_element(By.LINK_TEXT, 'Optional').click()
    for i in range(len(locators.list_op)):
        opt, ids, val = locators.list_op[i], locators.list_id[i], locators.list_val[i]
        print(f'Populate {opt} field')
        sleep(1)
        driver.find_element(By.ID, ids).send_keys(val)
        sleep(.25)
    ################################
    # press submit button
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(.25)
    print(f'----New User "{locators.new_username}/{locators.new_password}, {locators.email}" is added')

    ####################################


def search_user():
    # Check we are on users main page
    if driver.current_url == locators.moodle_users_main_page and driver.title == locators.moodle_users_main_page_title:
        assert driver.find_element(By.LINK_TEXT,
                                   'Browse list of users').is_displayed(), 'NOT AT THE LIST_OF _USERS PAGE'
        print(f'Browse list of users page is displayed')
        sleep(1)
        # Search we can check user by email
        print(f'---- Search for user by email address: {locators.email}------')
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
        if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
            print(f'---- User: {locators.email} is  found')


def check_new_user_can_login():
    if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(.,"{locators.full_name}")]').is_displayed():
            print(f'---- User with full name: {locators.first_name} is displayed')
    logger('created')


def delete_user():
    # navigate to the site administration
    sleep(5)
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(1)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(2)

    search_user()
    sleep(2)
    driver.find_element(By.XPATH, '//*[contains(@title,"Delete")]').click()
    sleep(.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Delete")]').click()
    sleep(1)
    print(f'*********New user deleted. Username: {locators.new_username} and Email: {locators.email}******')
    logger('deleted')


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()

# setup()
# #-----create new user=---------
# log_in(locators.admin_user_name,locators.admin_password) #LOGIN As Admin
# create_new_user()
# search_user()
# log_out()
# #-----------------------------------------
# #---------Login As New User---------------
#
# log_in(locators.new_username,locators.new_password)
# check_new_user_can_login()
# logger('created')
# log_out()
# #-----------------------------------------
# #----------Delete the new User------------
# log_in(locators.admin_user_name,locators.admin_password)
# delete_user()
# log_out()
# #=-----------------------------------------------
# tearDown()
