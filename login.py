from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl

timecard = openpyxl.load_workbook('timecard.xlsx')
sheet = timecard.get_sheet_by_name('Sheet1')

baseurl = "https://www.fieldglass.net/login.do" 
username = "coolguy123" 
password = "123fakestreet"

elements_by_name = {
 'usernameTxtBox' : "username", 
 'passwordTxtBox' : "password", 
 'submitButton' : "action"
 }

elements_by_css = {
    'loginButton' : '.formLoginButton_new',
    'submitButton' : '.primaryButton'
}

timecard_boxes = {
 1 : "timein00",
 2 : "timein01",
 3 : "timein02",
 4 : "timein03",
 5 : "timein04",
 6 : "timein10",
 7 : "timein11",
 8 : "timein12",
 9 : "timein13",
 10 : "timein14",
 11 : "timein20",
 12 : "timein21",
 13 : "timein22",
 14 : "timein23",
 15 : "timein24",
 16 : "timein30",
 17 : "timein31",
 18 : "timein32",
 19 : "timein33",
 20 : "timein34"
 }

totalhours = {
    1 : "//input[@id='t_z13052120053200506563866_b_1_r1']",
    2 : "//input[@id='t_z13052120053200506563866_b_2_r1']",
    3 : "//input[@id='t_z13052120053200506563866_b_3_r1']",
    4 : "//input[@id='t_z13052120053200506563866_b_4_r1']",
    5 : "//input[@id='t_z13052120053200506563866_b_5_r1']"
    }

mydriver = webdriver.Firefox() 
mydriver.get(baseurl) 
mydriver.maximize_window()

# Clear Username TextBox if already allowed "Remember Me"
mydriver.find_element_by_name(elements_by_name['usernameTxtBox']).clear()

# Write Username in Username TextBox
mydriver.find_element_by_name(elements_by_name['usernameTxtBox']).send_keys(username)

# Clear Password TextBox if already allowed "Remember Me"
mydriver.find_element_by_name(elements_by_name['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_name(elements_by_name['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_css_selector(elements_by_css['loginButton']).click()

#enter timesheet page
mydriver.find_element_by_link_text(('Enter hours in Time Sheet')).click()


#keep count of which key you are on in the dictionary
number = 1

#enter hours in from timecard.xlsx
for rowOfCellObjects in sheet['B2':'F5']:
    for cellObj in rowOfCellObjects:
        mydriver.find_element_by_name(timecard_boxes[number]).send_keys(cellObj.value, Keys.TAB)
        #incrementing by one here as you want the actual value, not which row or column you are on
        number += 1

monHours = mydriver.find_element_by_id('t_tito_0').text
tueHours = mydriver.find_element_by_id('t_tito_1').text
wedHours = mydriver.find_element_by_id('t_tito_2').text
thuHours = mydriver.find_element_by_id('t_tito_3').text
friHours = mydriver.find_element_by_id('t_tito_4').text


mydriver.find_element_by_xpath("//input[@id='t_z13052120053200506563866_b_1_r1']").send_keys(monHours)
mydriver.find_element_by_xpath("//input[@id='t_z13052120053200506563866_b_2_r1']").send_keys(tueHours)
mydriver.find_element_by_xpath("//input[@id='t_z13052120053200506563866_b_3_r1']").send_keys(wedHours)
mydriver.find_element_by_xpath("//input[@id='t_z13052120053200506563866_b_4_r1']").send_keys(thuHours)
mydriver.find_element_by_xpath("//input[@id='t_z13052120053200506563866_b_5_r1']").send_keys(friHours)



mydriver.find_element_by_css_selector(elements_by_css['submitButton']).click()
