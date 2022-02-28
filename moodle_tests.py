import unittest
import moodle_locators as locators
import moodle_methods as methods


class MoodleAppPositiveTestCases(unittest.TestCase):   # create class

    @staticmethod  # signal to unittest that it is a static method
    def test_create_new_user():
        methods.setup()
        methods.log_in(locators.admin_user_name, locators.admin_password)
        methods.create_new_user()
        methods.search_user()
        methods.log_out()

        methods.log_in(locators.new_username, locators.new_password)
        methods.check_new_user_can_login()
        methods.log_out()

        methods.log_in(locators.admin_user_name, locators.admin_password)
        methods.delete_user()
        methods.log_out()
        methods.tearDown()


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
