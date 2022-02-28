from faker import Faker

fake = Faker(locale='en-CA')
# -------------------locators section--------------------
app = 'Moodle'
admin_user_name = 'tinubaby'
admin_password = 'Moodle!123'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_page_title = 'Dashboard'
moodle_add_new_user_page_title = 'SQA: Administration: Users: Accounts: Add a new user'
moodle_users_main_page='http://52.39.5.126/admin/user.php'
moodle_users_main_page_title= 'SQA: Administration: Users: Accounts: Browse list of users'

# --------------------data section---------------------------------------
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name}'

new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'

moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.current_country()
description = f'user added by {admin_user_name} via python selenium automatd script'  # fake.sentence(nb_words = 100)

pic_desc = f'Submitted by {full_name}'
list_of_interests = [fake.job(), fake.job(), fake.job(), fake.job(), fake.job()]
print(list_of_interests)

web_page = fake.url()
icq_num = fake.pyint(111111, 999999)
skype_id = new_username
aim_id = f'{last_name.lower()}{fake.pyint(11, 9999)}'
yahoo_id = new_username
msn_id = f'{last_name.lower()}{fake.pyint(11, 99)}{country}'
id_num = fake.pyint(1111111, 9999999)
institution = fake.company()
department = fake.catch_phrase()
phone = fake.phone_number()
mobile_phone = fake.phone_number()
address = fake.address().replace("\n", " ")
list_op = ['Web page', 'ICQ number', 'Skype ID', 'AIM ID', 'Yahoo ID', 'MSN ID',
           'ID number', 'Institution', 'Department',
           'Phone', 'Mobile phone', 'Address']

list_id = ['id_url', 'id_icq', 'id_skype', 'id_aim', 'id_yahoo', 'id_msn',
           'id_idnumber', 'id_institution', 'id_department',
           'id_phone1', 'id_phone2', 'id_address']

list_val = [web_page, icq_num, skype_id, aim_id, yahoo_id, msn_id,
            id_num, institution, department,
            phone, mobile_phone, address]
print(list_val)

print(
    f'\nFirst Name: {first_name},\nLast Name: {last_name},\nMiddle Name: {middle_name},\nPassword: {new_password},\nEmail: {email}')
